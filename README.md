Create a NetBox config template called ipxe:

```
#!ipxe

kernel http://foo.bar/{{ device.platform.slug }}/vmlinuz
initrd http://foo.bar/images/{{ device.platform.slug }}/initrd.img
boot
```

Build and run this container

Retrieve the ipxe script:

```
curl -X GET "http://localhost:8080?asset_tag=ABC123"
```

For development, run the flask app directly:

```
flask --app www/wsgi.py --debug run
```