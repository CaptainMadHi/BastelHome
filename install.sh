activate() {
  . "./venv/bin/activate"
}

python3 -m venv venv            # setup venv
activate                        # activate venv
pip install -r requirements.txt # install python packages into venv

curl -L https://raw.githubusercontent.com/tj/n/master/bin/n -o n #install node & npm
bash n lts
rm n

cd "./frontend"                 
npm install                     # install JavaScript packages
npm run build                   # build the website
cd ".."
# setup scripts go here ?

# maybe already start the connected component ? 