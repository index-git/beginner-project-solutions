.PHONY: test

version_tuple := $(subst ., ,$(version:%=%))
version_major := $(word 1,$(version_tuple))
version_minor := $(word 2,$(version_tuple))
version_patch := $(word 3,$(version_tuple))
$(eval version_minor_next=$(shell echo $$(($(version_minor)+1))))
$(eval version_patch_next=$(shell echo $$(($(version_patch)+1))))

else:
	echo "Nothing to do."

tag:
	echo "Version=$(version)" > _version.py
	git add _version.py
	git commit -m "Release $(version)"
	git tag -a "v$(version)" -m "v$(version)"
	git push origin "v$(version)"
	echo "Version=$(version_major).$(version_minor_next).$(version_patch)-dev" > _version.py
	git commit -m "Starting development of $(version_major).$(version_minor_next).$(version_patch)-dev"

tag-patch:
	echo "Version=$(version)" > _version.py
	git add _version.py
	git tag -a "v$(version)" -m "v$(version)"
	git push origin "v$(version)"
	echo "Version=$(version_major).$(version_minor).$(version_patch_next)-dev" > _version.py
