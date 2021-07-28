console.log("JavaScript is connected!")

function imageHover(element){
    element.src = "../Web_Fundamentals/graphics/succulents-2.jpg";
}

function imageHoverOut(element){
    element.src = "../Web_Fundamentals/graphics/succulents-1.jpg";
}

function cookiesHide(element){
    document.getElementById("cookiesBox").style.display = "none";
}
