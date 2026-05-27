from __future__ import annotations

import json
import os
import shutil
import subprocess


def _detect_docker_openfoam_images() -> list[dict]:
    docker_bin = shutil.which("docker")
    if not docker_bin:
        return []

    try:
        result = subprocess.run(
            [docker_bin, "images", "--format", "{{json .}}"],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return []

    if result.returncode != 0:
        return []

    images: list[dict] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue

        repo = (entry.get("Repository") or "").lower()
        tag = entry.get("Tag") or ""
        if "openfoam" in repo:
            images.append(
                {
                    "repository": entry.get("Repository"),
                    "tag": tag,
                    "image": f"{entry.get('Repository')}:{tag}",
                }
            )

    return images


def detect_openfoam() -> dict:
    cmds = {k: shutil.which(k) for k in ["blockMesh", "checkMesh", "icoFoam", "foamVersion"]}
    version = os.environ.get("WM_PROJECT_VERSION")
    distro = "unknown"
    if version and version.startswith("v"):
        distro = "openfoam.com"
    elif version:
        distro = "openfoam.org"

    docker_images = _detect_docker_openfoam_images()
    docker_status = "available" if docker_images else "not_found"

    return {
        "distribution": distro,
        "version": version,
        "commands": {k: v for k, v in cmds.items() if v},
        "environment": {
            "WM_PROJECT": os.environ.get("WM_PROJECT"),
            "WM_PROJECT_VERSION": version,
            "WM_PROJECT_DIR": os.environ.get("WM_PROJECT_DIR"),
            "FOAM_INST_DIR": os.environ.get("FOAM_INST_DIR"),
            "WM_COMPILER": os.environ.get("WM_COMPILER"),
            "WM_OPTIONS": os.environ.get("WM_OPTIONS"),
        },
        "docker": {
            "binary": shutil.which("docker"),
            "status": docker_status,
            "openfoam_images": docker_images,
        },
        "status": "usable" if cmds["blockMesh"] and cmds["checkMesh"] else ("docker_only" if docker_images else "unavailable"),
    }
