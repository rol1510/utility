if exist "%~dp0dist\" (
    cd dist
    del /f *
    cd ..
)
py setup.py sdist bdist_wheel
