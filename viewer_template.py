import json

def create_html_viewer(json_file_path, output_file="viewer.html"):
    # Load JSON from file
    with open(json_file_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    html_header = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Offline JSON Viewer</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f4f4f4;
      padding: 20px;
    }
    h1 {
      font-size: 24px;
      margin-bottom: 10px;
    }
    .legend {
      margin-bottom: 15px;
    }
    .legend span {
      padding: 6px 12px;
      margin-right: 10px;
      border-radius: 4px;
      font-size: 14px;
      color: #fff;
    }
    .rank-1-3 { background-color: #d9534f; }
    .rank-4-7 { background-color: #f0ad4e; }
    .rank-8-10 { background-color: #5bc0de; }
    .section {
      padding: 12px;
      border-left: 4px solid;
      background-color: #fff;
      margin-bottom: 10px;
      box-shadow: 0 0 6px rgba(0,0,0,0.1);
    }
    .rank-1 { border-color: #d9534f; }
    .rank-2, .rank-3 { border-color: #d9534f; }
    .rank-4, .rank-5, .rank-6, .rank-7 { border-color: #f0ad4e; }
    .rank-8, .rank-9, .rank-10 { border-color: #5bc0de; }
    .section strong {
      display: block;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <h1>Offline JSON Viewer (challenge1b_output.json)</h1>
  <div class="legend">
    <span class="rank-1-3">⭐ Rank 1–3 (High Importance)</span>
    <span class="rank-4-7">⭐ Rank 4–7 (Medium Importance)</span>
    <span class="rank-8-10">⭐ Rank 8–10 (Low Importance)</span>
  </div>
"""

    html_body = ""
    for section in json_data.get("extracted_sections", []):
        rank = section.get("importance_rank", 10)
        html_body += f"""
  <div class='section rank-{rank}'>
    📄 <strong>Document:</strong> {section['document']}<br>
    📃 <strong>Page:</strong> {section['page_number']}<br>
    📝 <strong>Title:</strong> {section['section_title']}<br>
    ⭐ <strong>Rank:</strong> {rank}
  </div>
"""

    html_footer = """
</body>
</html>"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_header + html_body + html_footer)

    print(f"🌐 HTML viewer saved as {output_file}")
