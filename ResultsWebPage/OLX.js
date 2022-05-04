fetch(`http://localhost:5000/filters`)
.then(data =>{
    document.getElementById("loading").remove();
    document.getElementById("content").style.display = "flex";
})


let filterFunctions = [filter0, filter1, filter2, filter3, filter4, filter5, filter6, filter7, filter8, filter9];
let resultBox = document.getElementById("filterResultBox");


async function getData(){
    const option = document.getElementById("filter-select");
    
    if(option.value === "none" && !document.getElementsByClassName("warning").length){
        resultBox.textContent = ""

        if (!resultBox.getElementsByTagName("span").length){
            const span = document.createElement("span")
            span.textContent = "Rezultatul va apărea aici."
            span.classList.add("message")

            resultBox.append(span)
        }

        const warning = document.createElement("div");
        warning.textContent = "Alegeți un filtru!";
        warning.classList.add("warning");
        
        document.body.append(warning);
        
        setTimeout(() =>{
            warning.remove();
        }, 1200)
    }

    else{
        for(var i = 0; i < filterFunctions.length; ++i)
            if(option.value == filterFunctions[i].name)
                resultBox.innerText = await filterFunctions[i]();
    }
}


async function filter0() {
    return await
    fetch(`../Server/Results/filter0.txt`)
    .then(response => response.text())
    
    .then(data => data)
}

async function filter1() {
    return await
    fetch(`../Server/Results/filter1.txt`)
    .then(response => response.text())
    
    .then(data => data)
}

async function filter2() {
    return await
    fetch(`../Server/Results/filter2.txt`)
    .then(response => response.text())
    
    .then(data => data)
}

async function filter3() {
    return await
    fetch(`../Server/Results/filter3.txt`)
    .then(response => response.text())
    
    .then(data => data)
}

async function filter4() {
    return await
    fetch(`../Server/Results/filter4.txt`)
    .then(response => response.text())
    
    .then(data => data)
}

async function filter5() {
    return await
    fetch(`../Server/Results/filter5.txt`)
    .then(response => response.text())
    
    .then(data => data)
}

async function filter6() {
    return await
    fetch(`../Server/Results/filter6.txt`)
    .then(response => response.text())
    
    .then(data => data)
}

async function filter7() {
    return await
    fetch(`../Server/Results/filter7.txt`)
    .then(response => response.text())
    
    .then(data => data)
}

async function filter8() {
    return await
    fetch(`../Server/Results/filter8.txt`)
    .then(response => response.text())
    
    .then(data => data)
}

async function filter9() {
    return await
    fetch(`../Server/Results/filter9.txt`)
    .then(response => response.text())
    
    .then(data => data)
}
