from flask import Flask, render_template, render_template_string
from markupsafe import escape
import pynetbox

nb = pynetbox.api(
    "https://demo.netbox.dev", token="bdca56791a60d69dc36a10b7b61806a1569a6756"
)

app = Flask(__name__)


@app.route("/")
@app.route("/<serial>", methods=["GET"])
def ipxe(serial=None):
    if serial is not None:

        # Try and fetch the device from NetBox - dealing with it not being
        # found.
        try:
            device = nb.dcim.devices.get(serial__ic=serial)
        except ValueError:  # get() returns > 1 results
            return f"Serial number '{escape(serial)}' not unique"

        # Try and find the device's config_context - dealing with it being missubg
        # or there being no config context at all
        try:
            ipxe_lines = device.config_context["ipxe_lines"]
        except AttributeError:  # device == None
            return f"Device with serial number '{escape(serial)}' not found"
        except KeyError:  # config context does not define ipxe_lines
            return "No attribute 'ipxe_lines' found in device config context"

        # Check ipxe_lines is a bona-fide list of strings and not just a single string
        if str(ipxe_lines) == ipxe_lines:
            # got a single string
            ipxe_lines = [render_template_string(ipxe_lines, device=device)]
        else:
            # got list of ipxe_lines
            ipxe_lines = [
                render_template_string(line, device=device) for line in ipxe_lines
            ]

        return render_template("bootstrap.j2", lines="\n".join(ipxe_lines))

    return "No serial number supplied"
