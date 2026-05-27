from __future__ import annotations

import json
import sqlite3
import uuid
from pathlib import Path

from caseweaver_core.schemas.casespec import TrustLevel

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS memory_cases (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    solver_family TEXT NOT NULL,
    solver_version TEXT,
    solver_distribution TEXT,
    template_id TEXT,
    case_path TEXT,
    trust_level TEXT NOT NULL,
    created_at TEXT NOT NULL,
    imported_at TEXT NOT NULL,
    summary TEXT,
    normalized_spec_json TEXT,
    derived_values_json TEXT,
    validation_report_json TEXT
);
CREATE TABLE IF NOT EXISTS memory_runs (
    id TEXT PRIMARY KEY,
    case_id TEXT NOT NULL,
    status TEXT NOT NULL,
    solver_name TEXT,
    started_at TEXT,
    completed_at TEXT,
    command_json TEXT,
    log_path TEXT,
    residuals_json TEXT,
    metrics_json TEXT,
    FOREIGN KEY(case_id) REFERENCES memory_cases(id)
);
"""


class MemoryStore:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.executescript(SCHEMA_SQL)

    def import_case(self, case_path: str, summary: str = "") -> str:
        cid = str(uuid.uuid4())
        now = "2026-05-27T00:00:00Z"
        self.conn.execute(
            """INSERT INTO memory_cases
            (id,name,solver_family,solver_version,solver_distribution,template_id,case_path,trust_level,created_at,imported_at,summary,normalized_spec_json,derived_values_json,validation_report_json)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                cid,
                Path(case_path).name,
                "openfoam",
                None,
                None,
                "lid_driven_cavity",
                case_path,
                TrustLevel.UNVERIFIED.value,
                now,
                now,
                summary,
                json.dumps({}),
                json.dumps({}),
                json.dumps({"status": "imported"}),
            ),
        )
        self.conn.commit()
        return cid

    def list_cases(self) -> list[dict]:
        cur = self.conn.execute("SELECT id,name,trust_level,case_path FROM memory_cases ORDER BY imported_at DESC")
        return [{"id": r[0], "name": r[1], "trust_level": r[2], "case_path": r[3]} for r in cur.fetchall()]
