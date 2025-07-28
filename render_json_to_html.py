import json

# Read the output JSON
with open("challenge1b_output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Embed JSON into HTML safely
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Offline JSON Viewer</title>
  <style>
    body {{
      font-family: 'Courier New', monospace;
      background-color: #f8f9fa;
      padding: 20px;
    }}
    h1 {{
      font-size: 22px;
      color: #333;
    }}
    pre {{
      background-color: #fff;
      padding: 20px;
      border: 1px solid #ccc;
      overflow-x: auto;
      white-space: pre-wrap;
      word-wrap: break-word;
    }}
  </style>
</head>
<body>
  <h1>📁 challenge1b_output.json (Embedded View)</h1>
  <pre>{json.dumps(data, indent=2)}</pre>
</body>
</html>
"""

# Save to a file
with open("rendered_output.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML file created: rendered_output.html")
