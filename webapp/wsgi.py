from flask import Flask, request, render_template_string
import pynetbox

nb = pynetbox.api(
    'https://demo.netbox.dev',
    token='bdca56791a60d69dc36a10b7b61806a1569a6756'
)

app = Flask(__name__)

@app.route('/', methods=['GET'])
# def ipxe():
#     args = request.args
#     if 'asset_tag' in args:
#         print(f"Searching for {args['asset_tag']}")
#         device = nb.dcim.devices.get(asset_tag__ic=args['asset_tag'])
#         if device:
#             return device.render_config.create()['content']
#         return "Asset tag not found"
#     return "No asset_tag in query string"

def ipxe():
    args = request.args
    if 'asset_tag' in args:
        device = nb.dcim.devices.get(asset_tag__ic=args['asset_tag'])
        template = nb.extras.config_templates.get(name='ipxe.j2').template_code
        if device:
            return render_template_string(template, device=device)
        return "Asset tag not found"
    return "No asset_tag in query string"