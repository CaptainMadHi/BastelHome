sudo pip3 install -r requirements.txt # install python packages into venv

curl -L https://raw.githubusercontent.com/tj/n/master/bin/n -o n #install node & npm
sudo bash n lts
rm n

cd "./frontend"                 
npm install                     # install JavaScript packages
npm run build                   # build the website
cd ".."
# setup scripts go here ?

# maybe already start the connected component ? 