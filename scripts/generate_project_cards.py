"""
Generatore di card SVG individuali per ciascun progetto in assets/projects/
Mantiene lo stile terminale/cyberpunk di processes.svg, ma rende ogni card autonoma e cliccabile.
"""

import html
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "assets" / "projects"

PROJECTS = [
    {
        "pid": "PID 0001",
        "name": "java-music-playlist-manager",
        "tag": "[self-driven]",
        "lines": [
            "Desktop music player, JavaFX. Started as a",
            "Software Architecture exam project — still being extended",
            "for fun post-exam. Ports & Adapters, Factory, Command/Undo,",
            "125 unit tests, custom Persona-style UI theming engine."
        ],
        "repo_display": "github.com/CupoMeridio/Java-Music-Playlist-Manager",
        "repo_url": "https://github.com/CupoMeridio/Java-Music-Playlist-Manager",
        "filename": "pid-0001-java-music-playlist-manager.svg"
    },
    {
        "pid": "PID 0002",
        "name": "waste-type-classifier",
        "tag": "[exam · ml]",
        "lines": [
            "8-class waste image classification, PyTorch.",
            "Two-phase transfer learning across EfficientNet B0/B2/B3,",
            "temperature-scaled reject option for open-set recognition,",
            "Grad-CAM interpretability. Full experiment suite, not just",
            "a single trained model."
        ],
        "repo_display": "github.com/CupoMeridio/waste-type-classifier",
        "repo_url": "https://github.com/CupoMeridio/waste-type-classifier",
        "filename": "pid-0002-waste-type-classifier.svg"
    },
    {
        "pid": "PID 0003",
        "name": "granpremio-mivia-2025",
        "tag": "[exam · ai]",
        "lines": [
            "Autonomous driving for TORCS. Java client +",
            "KNN (KD-Tree) and MLP neural net over UDP, compared against",
            "a traditional rule-based driver as baseline."
        ],
        "repo_display": "github.com/CupoMeridio/Granpremio-MIVIA-2025",
        "repo_url": "https://github.com/CupoMeridio/Granpremio-MIVIA-2025",
        "filename": "pid-0003-granpremio-mivia-2025.svg"
    },
    {
        "pid": "PID 0004",
        "name": "unisafe-vote",
        "tag": "[exam · security]",
        "lines": [
            "E2E-verifiable e-voting proof of concept.",
            "RSA-OAEP + RSA-PSS, Merkle tree bulletin board, TLS between",
            "services, simulated attacks (MITM, replay, DoS) as test suite."
        ],
        "repo_display": "github.com/CupoMeridio/UniSafe-Vote",
        "repo_url": "https://github.com/CupoMeridio/UniSafe-Vote",
        "filename": "pid-0004-unisafe-vote.svg"
    },
    {
        "pid": "PID 0005",
        "name": "launchpad-online",
        "tag": "[self-driven]",
        "lines": [
            "Not an exam — built because I wanted a",
            "Launchpad performance tool. PWA, Web MIDI + Web Audio API,",
            "30+ built-in lighting animations, offline-capable."
        ],
        "repo_display": "github.com/CupoMeridio/Launchpad-Online",
        "repo_url": "https://github.com/CupoMeridio/Launchpad-Online",
        "filename": "pid-0005-launchpad-online.svg"
    },
    {
        "pid": "PID 0006",
        "name": "advanced_tc",
        "tag": "[internship]",
        "lines": [
            "Custom ERPNext/Frappe app: a real",
            "calendar UI for timesheet management, replacing the stock",
            "tabular view. Python backend, FullCalendar.js frontend,",
            "role-based project access control."
        ],
        "repo_display": "github.com/CupoMeridio/advanced_tc",
        "repo_url": "https://github.com/CupoMeridio/advanced_tc",
        "filename": "pid-0006-advanced-tc.svg"
    },
    {
        "pid": "PID 0007",
        "name": "stm32-hal-modular-drivers",
        "tag": "[exam · embedded]",
        "lines": [
            "OOP-style C drivers for STM32 (LED,",
            "button, FIFO queue, servo, RTC). Fully non-blocking, no",
            "HAL_Delay, null-pointer guarded throughout."
        ],
        "repo_display": "github.com/CupoMeridio/stm32-hal-modular-drivers",
        "repo_url": "https://github.com/CupoMeridio/stm32-hal-modular-drivers",
        "filename": "pid-0007-stm32-hal-modular-drivers.svg"
    },
    {
        "pid": "PID 0008",
        "name": "rubrica-java-mvc",
        "tag": "[exam]",
        "lines": [
            "Desktop contact manager, JavaFX + PostgreSQL.",
            "Full MVC architecture, DAO pattern for data persistence.",
            "Features: BCrypt auth, advanced search, and CSV export."
        ],
        "repo_display": "github.com/CupoMeridio/rubrica-java-mvc",
        "repo_url": "https://github.com/CupoMeridio/rubrica-java-mvc",
        "filename": "pid-0008-rubrica-java-mvc.svg"
    },
    {
        "pid": "PID 0009",
        "name": "wordageddon-g17",
        "tag": "[exam]",
        "lines": [
            "Educational JavaFX memory game on word frequencies.",
            "Multi-language document support and 4 quiz modes.",
            "PostgreSQL cloud db (Aiven) with MVC and DAO layers."
        ],
        "repo_display": "github.com/CupoMeridio/Wordageddon-G17",
        "repo_url": "https://github.com/CupoMeridio/Wordageddon-G17",
        "filename": "pid-0009-wordageddon-g17.svg"
    },
    {
        "pid": "PID 0010",
        "name": "beyond-reality-journeys",
        "tag": "[exam · web]",
        "lines": [
            "Fantasy trips booking platform in PHP 8, JS and MySQL.",
            "Stripe API for payments, FPDF for receipts, and AJAX",
            "for async interactions and real-time reviews."
        ],
        "repo_display": "github.com/CupoMeridio/beyond-reality-journeys",
        "repo_url": "https://github.com/CupoMeridio/beyond-reality-journeys",
        "filename": "pid-0010-beyond-reality-journeys.svg"
    },
    {
        "pid": "PID 0011",
        "name": "vinyl-collection-app",
        "tag": "[exam · mobile]",
        "lines": [
            "Flutter mobile app for managing vinyl collections.",
            "SQLite database, Provider state management, charts (fl_chart),",
            "and Singleton/Repository patterns. Full CRUD and image upload."
        ],
        "repo_display": "github.com/CupoMeridio/vinyl_collection_app_gruppo_16",
        "repo_url": "https://github.com/CupoMeridio/vinyl_collection_app_gruppo_16",
        "filename": "pid-0011-vinyl-collection-app.svg"
    },
]

def render_card(proj: dict) -> str:
    line_count = len(proj["lines"])
    # y=30 header, y=55 riga 1, +20 per ogni riga successiva, +24 per link, +18 padding inferiore
    svg_height = 55 + (line_count * 20) + 30
    svg_width = 650

    safe_pid = html.escape(proj["pid"], quote=True)
    safe_name = html.escape(proj["name"], quote=True)
    safe_tag = html.escape(proj["tag"], quote=True)
    safe_link = html.escape(proj["repo_display"], quote=True)

    used_len = len(proj["pid"]) + 4 + len(proj["name"]) + 1 + 10
    dash_count = max(4, 66 - used_len)
    dashes = "─" * dash_count

    body_texts = []
    for i, line in enumerate(proj["lines"]):
        y_pos = 55 + (i * 20)
        safe_line = html.escape(line, quote=True)
        if i == 0:
            body_texts.append(
                f'  <text class="text" x="20" y="{y_pos}" xml:space="preserve"><tspan class="tree">   │</tspan>  <tspan class="tags">{safe_tag}</tspan>  {safe_line}</text>'
            )
        else:
            body_texts.append(
                f'  <text class="text" x="20" y="{y_pos}" xml:space="preserve"><tspan class="tree">   │</tspan>  {safe_line}</text>'
            )

    link_y = 55 + (line_count * 20) + 4
    body_texts.append(
        f'  <text class="text" x="20" y="{link_y}" xml:space="preserve"><tspan class="tree">   └─→</tspan> <tspan class="link">{safe_link}</tspan> <tspan class="accent">↗</tspan></text>'
    )

    body_svg = "\n".join(body_texts)

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">
  <style>
    .card-bg {{
      fill: #050505;
      stroke: #161b22;
      stroke-width: 1px;
    }}
    .border-glow {{
      stroke: #0AFFB0;
      stroke-opacity: 0.22;
      stroke-width: 1px;
      fill: none;
    }}
    .text {{
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 14px;
      fill: #ffffff;
    }}
    .accent {{ fill: #0AFFB0; }}
    .tree {{ fill: #444444; }}
    .tags {{ fill: #ffbd2e; }}
    .link {{ fill: #58a6ff; font-weight: 500; }}
    .status {{
      animation: pulse 2s infinite alternate;
    }}
    @keyframes pulse {{
      0% {{ opacity: 0.7; }}
      100% {{ opacity: 1; }}
    }}
  </style>

  <defs>
    <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="2" fill="#0AFFB0" fill-opacity="0.03" />
    </pattern>
  </defs>

  <!-- Background card con bordo cyberpunk sottile -->
  <rect class="card-bg" x="0.5" y="0.5" width="{svg_width - 1}" height="{svg_height - 1}" rx="8" />
  <rect class="border-glow" x="0.5" y="0.5" width="{svg_width - 1}" height="{svg_height - 1}" rx="8" />
  
  <!-- Scanlines animate -->
  <rect width="100%" height="100%" fill="url(#scanlines)" rx="8">
    <animateTransform attributeName="transform" type="translate" values="0,0; 0,-4" dur="2s" repeatCount="indefinite" />
  </rect>

  <!-- Header processo -->
  <text class="text" x="20" y="30" xml:space="preserve">{safe_pid} ── <tspan class="accent">{safe_name}</tspan> {dashes} <tspan class="accent status">[RUNNING]</tspan></text>

  <!-- Contenuto descrittivo e link -->
{body_svg}
</svg>'''
    return svg_content

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for proj in PROJECTS:
        content = render_card(proj)
        out_path = OUTPUT_DIR / proj["filename"]
        out_path.write_text(content, encoding="utf-8")
        print(f"[✓] {proj['pid']} -> {out_path.name}")
    print(f"\\n[✓] Generate con successo {len(PROJECTS)} card in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
