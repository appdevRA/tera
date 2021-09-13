// getting all required elements
const ulTag = document.querySelector(".ulclass");
let totalPages = 20;
const searchWrapper = document.querySelector(".search");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const button = searchWrapper.querySelector(".button");
let linkTag = searchWrapper.querySelector("a");
let webLink;

// if user press any key and release
inputBox.onkeyup = (e)=>{
    let userData = e.target.value; //user entered data
    let emptyArray = [];
    if(userData){
        button.onclick = ()=>{
            webLink = "https://www.google.com/" + userData;
            linkTag.setAttribute("href", webLink);
            console.log(webLink);
            linkTag.click();
        }
        emptyArray = suggestions.filter((data)=>{
            //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase()); 
        });
        emptyArray = emptyArray.map((data)=>{
            // passing return data inside li tag
            return data = '<li>'+ data +'</li>';
        });
        searchWrapper.classList.add("active"); //show autocomplete box
        showSuggestions(emptyArray);
        let allList = suggBox.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            //adding onclick attribute in all li tag
            allList[i].setAttribute("onclick", "select(this)");
        }
    }else{
        searchWrapper.classList.remove("active"); //hide autocomplete box
    }
}

function select(element){
    let selectData = element.textContent;
    inputBox.value = selectData;
    button.onclick = ()=>{
        webLink = "https://www.google.com/search?q=" + selectData;
        linkTag.setAttribute("href", webLink);
        linkTag.click();
    }
    searchWrapper.classList.remove("active");
}

function showSuggestions(list){
    let listData;
    if(!list.length){
        userValue = inputBox.value;
        listData = '<li>'+ userValue +'</li>';
    }else{
        listData = list.join('');
    }
    suggBox.innerHTML = listData;
}

function element(totalPages, page) {
    let liTag = '';
    let activeLi;
    let beforePages = page - 1;
    let afterPages = page + 1;
    if(page > 1) { //if page value is greater than 1 then add new li which is the previous button
        liTag += `<li class="btn prev" onclick="element(totalPages, ${page - 1})"><span><i class="fas fa-angle-left"></i>Prev</span></li>`;
    }
    if (page > 2) { //if page value is greater than 2 then add new li tag with 1 value
        liTag += `<li class="numb" onclick="element(totalPages, 1)"><span>1</span></li>`;
        if (page > 3) { //if page value is greater than 3 then add new li tag with (...)
            liTag += `<li class="dots"><span>...</span></li>`;
        }
    }

    //how many pages or li show before the current li
    if (page == totalPages) { //if page value is equal to totalPages then subtract by -2 to the beforePages value
        beforePages = beforePages - 2;
    }else if (page == totalPages - 1) { //else if page value is equal to totalPages by -1 then subtract by -1 to the beforePages value
        beforePages = beforePages - 1;
    }

     //how many pages or li show after the current li
    if (page == 1) { //if page value is equal to 1 then add by +2 to the afterPages value
        afterPages = afterPages + 2;
    }else if (page == 2) { //else if page value is equal to 2 then add by +1 to the afterPages value
        afterPages = afterPages + 1;
    }

    for (let pageLength = beforePages; pageLength <= afterPages; pageLength++) {
        if (pageLength > totalPages) {
            continue;
        }
        if (pageLength == 0) { //if pageLength is equal to 0 then add +1 to the pagelength value
            pageLength = pageLength + 1;
        }
        if (page == pageLength) { //if page value is equal to pageLength then assign the active string in the activeLi variable
            activeLi = "active";
        }else{ //else leave empty to the activeLi variable
            activeLi = "";
        }
        liTag += `<li class="numb ${activeLi}" onclick="element(totalPages, ${pageLength})"><span>${pageLength}</span></li>`;
    }

    if (page < totalPages - 1) { //if page value is less than totalPages by -1 then show the last li or page which is 20
        if (page < totalPages - 2) { //if page value is less than totalPages by -2 then show the last (...) before last page
            liTag += `<li class="dots"><span>...</span></li>`;
        }
        liTag += `<li class="numb" onclick="element(totalPages, ${totalPages})"><span>${totalPages}</span></li>`;
    }


    if(page < totalPages) { //if page value is less than totalPages then add new li which is the next button
        liTag += `<li class="btn next" onclick="element(totalPages, ${page + 1})"><span>Next<i class="fas fa-angle-right"></i></span></li>`;
    }
    ulTag.innerHTML = liTag;
}
element(totalPages, 5); //calling above function with passing values

