let navBars = document.getElementById('header-navbars-id');
let headerNavList = document.getElementsByClassName('header-navigation-item');
let headerNav = document.getElementById('header-anchor');
let headerNavMenu = document.getElementById('header-navigation-id');
let signContainer = document.getElementById('sign-container-id');
if (screen.width <= 480) {
    navBars.style.display = "block";
    for(let i = 0; i < headerNavList.length;i++) {
        headerNavList[i].classList.add('navUnHide')
    }
    navBars.classList.add('hide');
    navBars.addEventListener('click',function () {
        for(let i = 0; i < headerNavList.length;i++) {
            headerNavList[i].classList.remove('navUnHide');
            headerNavList[i].classList.add('wow');
            headerNavList[i].classList.add('fadeIn');
        }
        headerNavMenu.classList.add('navMediaMenu');
        navBars.addEventListener('click',function () {
            for(let i = 0; i < headerNavList.length;i++) {
                headerNavList[i].classList.add('navUnHide');
            }
        })
    });
}

