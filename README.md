Define one of more config context templates containing an attribute ipxe_lines

```
kernel http://foo.bar/{{ device.platform.slug }}/vmlinuz
initrd http://foo.bar/images/{{ device.platform.slug }}/initrd.img
```

Apply this config context to candidate objects as appropriate.

Build and run this container

Retrieve the ipxe script:

```
curl -X GET "http://localhost:8080/ABC123"
```

For development, run the flask app directly:

```
flask --app www/wsgi.py --debug run
```