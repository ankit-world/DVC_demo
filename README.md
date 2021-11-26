create env

```bash
conda create -n wineq python==3.7 -y
```

activate env

```bash
conda activate wineq
```

create a requirement.txt file
install the requirement

```bash
pip install -r requirements.txt
```

download the data from

```bash
https://drive.google.com/file/d/1SD_BEBNwT6col-6hTkwgd1dDAT-fzKwd/view?usp=sharing
```

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given/winequality.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

one line updates for readme

```bash
git add . && git commit -m "update Readme.md"
```

Adding local to remote GitHub repo

```bash
git remote add origin https://github.com/ankit-world/DVC_demo.git
```

```bash
git branch -M main
```

```bash
git push -u origin main
```

tox command
```bash
tox
```

for rebuilding
```bash
tox -r
```

pytest command
```bash
pytest -v
```

setup commands
```buildoutcfg
pip install -e.
```

build your own package command
```buildoutcfg
python setup.py sdist bdist_wheel
```
