# entr RPM package on openEuler

[entr](http://eradman.com/entrproject/) is a file watcher,
which run specified commands when target files change.

# Build Package

To build a RPM package, create packaging scaffold with `rpmdev-setuptree`
if it doesn't exist.
Then copy entr-4.5.tar.gz ([upstream URL](http://eradman.com/entrproject/code/entr-4.5.tar.gz))
to ~/rpmbuild/SOURCES, entr.spec to ~/rpmbuild/SPECS, and run:
```
rpmlint entr.spec
rpmbuild -bs entr.spec
rpmbuild -bb entr.spec
```

Verified on openEuler 20.03 (LTS), Jun 4, 2020.

