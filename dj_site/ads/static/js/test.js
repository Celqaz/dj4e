function PartyAnimal() {
    this.x = 0
    this.party = function () {
        this.x = this.x + 1;
        console.log("So far " + this.x);
    }
}

function funprova() {
    alert("Hello! I am an alert box from remote js file!!");
    this.x = 'Glad You Come'

    for (let i = 0; i < 3; i++) {
        document.write("<h1>" + this.x + "<h1>")
    }

}

an = new PartyAnimal()
an.party()
an.party()
an.party()