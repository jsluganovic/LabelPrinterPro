// scripts that checks for new files being received. 

// > Creating temporary folders.
// > Deleteing them after userinput on website? 



// Imports


function checkNewRequest() {
    // idk yet 
    
    pass
    
}

function cretaeTempFolder(req_number) {
    x = os.path.exists("data/req/{req_number}/")

    if (x == true) {
        pass
    }
    if (x != true) {
        os.mkdir("data/req/{req_number}/")
    }
    

}

function deleteTempFolder(req_number) {
    x = os.path.exists("data/req/{req_number}/")

    if (x == true) {
        os.rmdir("data/req/{req_number}/")
    }
    if (x != true) {
        pass
    }
    

}