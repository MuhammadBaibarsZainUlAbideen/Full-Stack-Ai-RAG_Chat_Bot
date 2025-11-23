<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>RAG Full-Stack Chatbot — Visual README</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#9aa4b2; --accent:#7c3aed; --glass: rgba(255,255,255,0.04);
      --success:#10b981; --danger:#ef4444; --glass-2: rgba(255,255,255,0.02);
    }
    *{box-sizing:border-box}
    body{margin:0; font-family:Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; background:linear-gradient(180deg,#071024 0%, #071326 100%); color:#e6eef6; -webkit-font-smoothing:antialiased}
    .wrap{max-width:980px;margin:36px auto;padding:28px;border-radius:14px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));box-shadow:0 12px 40px rgba(2,6,23,0.6);border:1px solid rgba(255,255,255,0.03)}
    header{display:flex;gap:16px;align-items:center}
    .logo{width:64px;height:64px;flex:0 0 64px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#06b6d4);display:grid;place-items:center;color:white;font-weight:700}
    h1{margin:0;font-size:20px}
    p.lead{margin:6px 0 18px;color:var(--muted)}

    .grid{display:grid;grid-template-columns:1fr 360px;gap:20px}
    @media (max-width:880px){.grid{grid-template-columns:1fr}}

    .card{background:var(--card);padding:18px;border-radius:12px;border:1px solid var(--glass);}
    .section-title{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}

    .skills{display:flex;flex-direction:column;gap:12px}
    .skill{display:flex;flex-direction:column;gap:8px}
    .skill-row{display:flex;align-items:center;gap:12px}
    .meta{width:160px;display:flex;flex-direction:column}
    .meta strong{font-size:14px}
    .meta small{color:var(--muted);font-size:12px}

    .bar-wrap{flex:1;background:var(--glass-2);padding:8px;border-radius:10px}
    .bar{height:18px;border-radius:8px;background:linear-gradient(90deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04));position:relative;overflow:hidden}
    .bar > i{display:block;height:100%;width:0%;border-radius:8px;background:linear-gradient(90deg,var(--accent),#06b6d4);box-shadow:0 6px 18px rgba(124,58,237,0.18);transition:width 900ms cubic-bezier(.2,.9,.3,1)}
    .bar[data-danger] > i{background:linear-gradient(90deg,var(--danger),#fb923c)}

    .label-right{min-width:90px;text-align:right;font-size:13px;color:var(--muted)}

    .details{line-height:1.45;color:var(--muted);font-size:14px}
    .pill{display:inline-flex;gap:8px;align-items:center;background:rgba(255,255,255,0.02);padding:8px 10px;border-radius:999px;border:1px solid rgba(255,255,255,0.03)}

    .legend{display:flex;gap:8px;flex-wrap:wrap}
    .legend .item{display:flex;gap:8px;align-items:center;padding:6px 10px;border-radius:8px;background:rgba(255,255,255,0.01);border:1px solid rgba(255,255,255,0.02);font-size:13px}
    .sw{width:12px;height:12px;border-radius:4px}

    footer{margin-top:16px;display:flex;justify-content:space-between;align-items:center}
    .btn{background:transparent;border:1px solid rgba(255,255,255,0.06);padding:8px 12px;border-radius:8px;color:var(--muted);cursor:pointer}
    .btn:active{transform:translateY(1px)}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">RAG</div>
      <div>
        <h1>RAG Full-Stack Chatbot — visual README</h1>
        <p class="lead">A compact visual README to show strengths of the project components. Copy this file into your repo (README_visual.html) and link to it from your README.md.</p>
      </div>
    </header>

    <div class="grid" style="margin-top:18px">
      <div>
        <div class="card">
          <div class="section-title">
            <div>
              <strong>Skill Overview</strong>
              <div style="font-size:13px;color:var(--muted)">Bars show confidence/coverage of each area</div>
            </div>
            <div class="pill">🔧 Tech: HTML • CSS • JS • Python • LangChain • Pinecone</div>
          </div>

          <div class="skills" id="skills">
            <div class="skill">
              <div class="skill-row">
                <div class="meta"><strong>Full Stack</strong><small>Project-wide orchestration</small></div>
                <div class="bar-wrap">
                  <div class="bar" data-value="90"><i></i></div>
                </div>
                <div class="label-right">90% — Almost full</div>
              </div>
            </div>

            <div class="skill">
              <div class="skill-row">
                <div class="meta"><strong>Backend</strong><small>API, RAG glue, worker processes</small></div>
                <div class="bar-wrap">
                  <div class="bar" data-value="88"><i></i></div>
                </div>
                <div class="label-right">88% — Almost full</div>
              </div>
            </div>

            <div class="skill">
              <div class="skill-row">
                <div class="meta"><strong>Frontend</strong><small>UI, chat, UX polish</small></div>
                <div class="bar-wrap">
                  <div class="bar" data-value="87"><i></i></div>
                </div>
                <div class="label-right">87% — Almost full</div>
              </div>
            </div>

            <div class="skill">
              <div class="skill-row">
                <div class="meta"><strong>RAG Pipeline</strong><small>Vector store, retriever, prompt templates</small></div>
                <div class="bar-wrap">
                  <div class="bar" data-value="100"><i></i></div>
                </div>
                <div class="label-right">100% — Full</div>
              </div>
            </div>

            <div class="skill">
              <div class="skill-row">
                <div class="meta"><strong>Database</strong><small>Persistence, metadata, versioning</small></div>
                <div class="bar-wrap">
                  <div class="bar" data-value="95"><i></i></div>
                </div>
                <div class="label-right">95% — Almost full</div>
              </div>
            </div>

            <div class="skill">
              <div class="skill-row">
                <div class="meta"><strong>Authentication</strong><small>OAuth, JWT, session handling</small></div>
                <div class="bar-wrap">
                  <div class="bar" data-value="84" data-danger><i></i></div>
                </div>
                <div class="label-right">84% — Slightly less than almost full</div>
              </div>
            </div>

          </div>

          <footer>
            <div class="legend">
              <div class="item"><span class="sw" style="background:linear-gradient(90deg,var(--accent),#06b6d4)"></span>Primary</div>
              <div class="item"><span class="sw" style="background:linear-gradient(90deg,var(--danger),#fb923c)"></span>Needs attention</div>
            </div>
            <div>
              <button class="btn" id="copyBtn">Copy Markdown Snippet</button>
            </div>
          </footer>

        </div>

        <div style="height:16px"></div>

        <div class="card">
          <strong>How to use</strong>
          <div class="details" style="margin-top:8px">
            1. Drop this file into your repo and link from your README.md: <code>&lt;a href=\"./README_visual.html\"&gt;Project visual README&lt;/a&gt;</code>.
            <br>2. Edit the <code>data-value</code> attributes to reflect your real strengths.
            <br>3. The bars animate on load. You can change colors in :root or replace the gradient.
          </div>
        </div>
      </div>

      <div>
        <div class="card">
          <strong>Live Summary</strong>
          <div class="details" style="margin-top:10px">
            This panel mirrors the bars and gives a short status description for each component of your RAG full-stack chatbot.
          </div>

          <div style="margin-top:12px;display:flex;flex-direction:column;gap:10px">
            <div class="card" style="background:linear-gradient(180deg, rgba(255,255,255,0.01), transparent);padding:12px">
              <strong>RAG Pipeline</strong>
              <div style="font-size:13px;color:var(--muted);margin-top:6px">Retriever tuned, vector store integrated, prompt batching, fallback to LLM for low-confidence answers.</div>
            </div>
            <div class="card" style="padding:12px">
              <strong>Deployment notes</strong>
              <div style="font-size:13px;color:var(--muted);margin-top:6px">Containerize workers, keep vector DB backups, rotate LLM keys, secure auth endpoints.</div>
            </div>
          </div>
        </div>

        <div style="height:12px"></div>

        <div class="card">
          <strong>Quick tweak</strong>
          <div class="details" style="margin-top:8px">To change a value, edit <code>data-value="XX"</code> on the .bar element (0–100) and update the right-side text. Bars animate to that width on load.</div>
        </div>
      </div>
    </div>
  </div>

  <script>
    function animateBars(){
      document.querySelectorAll('.bar').forEach(bar => {
        const v = Number(bar.getAttribute('data-value') || 0);
        const inner = bar.querySelector('i');
        // clamp 0-100
        const pct = Math.max(0, Math.min(100, v));
        // small delay for nicer stagger
        setTimeout(()=> inner.style.width = pct + '%', 120);
      });
    }

    // Copy a short markdown snippet to clipboard
    document.getElementById('copyBtn').addEventListener('click', async ()=>{
      const md = `### Visual project status\n[Open the visual README](./README_visual.html) — shows Full Stack, Backend, Frontend, RAG Pipeline, Database, Authentication with progress bars.`;
      try{
        await navigator.clipboard.writeText(md);
        document.getElementById('copyBtn').textContent = 'Copied!';
        setTimeout(()=> document.getElementById('copyBtn').textContent = 'Copy Markdown Snippet', 1600);
      }catch(e){ alert('Could not copy to clipboard — you can manually copy the snippet.'); }
    });

    window.addEventListener('load', animateBars);
  </script>
</body>
</html>
