const memoryCases = [
  { name: "cavity_Re100_50x50", trust: "RUN_VALID", version: "v2312", similarity: "91%", usedFor: "deltaT, mesh, fvSolution" },
  { name: "cavity_Re400_100x100", trust: "USER_APPROVED", version: "11", similarity: "84%", usedFor: "high-Re warning" },
  { name: "cavity_Re1000_120x120", trust: "GOLDEN_CASE", version: "v2512", similarity: "80%", usedFor: "stability numerics" },
];

export function AppShell() {
  return (
    <div className="mx-auto max-w-7xl p-6 text-slate-100 md:p-10">
      <header className="glass mb-6 rounded-3xl p-6">
        <p className="text-sky-300">Local AI case generation for CFD solvers.</p>
        <h1 className="mt-1 text-4xl font-bold">Caseweaver</h1>
        <p className="mt-3 max-w-3xl text-slate-300">
          The LLM suggests. The schema validates. The generator writes. The solver verifies. The memory improves future context.
        </p>
      </header>

      <div className="grid gap-6 lg:grid-cols-3">
        <section className="glass rounded-2xl p-5 lg:col-span-2">
          <h2 className="text-xl font-semibold">Case Generator</h2>
          <p className="mb-4 text-sm text-slate-300">Describe the case in natural language and get validated, deterministic OpenFOAM files.</p>
          <div className="rounded-xl border border-slate-600/40 bg-slate-900/40 p-4">
            <p className="text-sm text-slate-400">Prompt</p>
            <p className="mt-1">Make a Re 1000 lid-driven cavity with stable mesh and OpenFOAM.com v2512 compatibility.</p>
          </div>
          <div className="mt-4 grid gap-3 sm:grid-cols-2">
            <Metric title="Template" value="lid_driven_cavity" />
            <Metric title="Suggested mesh" value="120x120x1" />
            <Metric title="Suggested deltaT" value="0.0005" />
            <Metric title="Environment" value="Docker v2512" />
          </div>
        </section>

        <section className="glass rounded-2xl p-5">
          <h2 className="text-xl font-semibold">OpenFOAM Manager</h2>
          <ul className="mt-3 space-y-2 text-sm text-slate-200">
            <li>Distribution: <span className="text-sky-300">OpenFOAM.com</span></li>
            <li>Version: <span className="text-sky-300">v2512</span></li>
            <li>Status: <span className="text-emerald-300">docker_only</span></li>
            <li>Docker image: <span className="text-sky-300">openfoam/openfoam-v2512</span></li>
          </ul>
          <button className="mt-4 w-full rounded-xl bg-sky-500/80 px-4 py-2 font-medium text-white hover:bg-sky-500">Validate Environment</button>
        </section>
      </div>

      <section className="glass mt-6 rounded-2xl p-5">
        <div className="mb-4 flex items-center justify-between">
          <h2 className="text-xl font-semibold">Relevant Memory</h2>
          <span className="rounded-full bg-emerald-500/20 px-3 py-1 text-xs text-emerald-300">3 similar valid cases found</span>
        </div>
        <div className="grid gap-3 md:grid-cols-3">
          {memoryCases.map((m) => (
            <article key={m.name} className="rounded-xl border border-slate-600/40 bg-slate-900/35 p-4">
              <h3 className="font-semibold">{m.name}</h3>
              <p className="text-sm text-slate-300">{m.trust} • OpenFOAM {m.version}</p>
              <p className="mt-1 text-sm text-slate-300">Similarity: {m.similarity}</p>
              <p className="mt-2 text-xs text-slate-400">Used for: {m.usedFor}</p>
              <div className="mt-3 flex gap-2 text-xs">
                <button className="rounded-lg bg-slate-700/80 px-2 py-1">Use</button>
                <button className="rounded-lg bg-slate-700/80 px-2 py-1">Ignore</button>
                <button className="rounded-lg bg-amber-600/70 px-2 py-1">Promote</button>
              </div>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}

function Metric({ title, value }: { title: string; value: string }) {
  return (
    <div className="rounded-xl border border-slate-600/40 bg-slate-900/35 p-3">
      <p className="text-xs uppercase tracking-wider text-slate-400">{title}</p>
      <p className="mt-1 font-semibold">{value}</p>
    </div>
  );
}
