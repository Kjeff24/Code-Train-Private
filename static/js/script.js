const bar = document.getElementById('bar');
const nav = document.getElementById('navbar');
const close = document.getElementById('close');

if(bar){
    bar.addEventListener('click', () => {
        nav.classList.add('active');
    })
}
if(close){
    close.addEventListener('click', () => {
        nav.classList.remove('active');
    })
}

// start of verification page
const otpInputs = document.querySelectorAll('.otp-bx input');
const errorMessage = document.querySelector('#error-message');

for (let i = 0; i < otpInputs.length; i++) {
    otpInputs[i].addEventListener('input', e => {
      const input = e.target;
      const nextInput = otpInputs[i + 1];
      if (input.value !== '') {
        input.classList.add('filled');
        if (nextInput) {
          nextInput.focus();
        }
      } else {
        input.classList.remove('filled');
      }
    });

    otpInputs[i].addEventListener('keydown', e => {
        const input = e.target;
        const prevInput = otpInputs[i - 1];
        const nextInput = otpInputs[i + 1];
    
        if (e.key === 'Backspace') {
          input.value = '';
          input.classList.remove('filled');
    
          if (prevInput) {
            prevInput.focus();
          }
        }
      });

}





// document.addEventListener('DOMContentLoaded', () => {
//     otpInputs[0].focus();
// });

// document.querySelector('#otp-form').addEventListener('submit', e => {
//     e.preventDefault();
//     const otp = Array.from(otpInputs).map(input => input.value).join('');
//     if (otp === '') {
//       errorMessage.textContent = 'Please enter OTP';
//       return;
//     }
//     if (otp.length !== 4) {
//       errorMessage.textContent = 'OTP should be 4 digits';
//       return;
//     }
//     if (!/^\d+$/.test(otp)) {
//       errorMessage.textContent = 'OTP should contain only digits';
//       return;
//     }
// });

// end of verification page


// start of add to cart
// const cartCount = document.querySelector('.cart-count');
// // replace 0 with the actual cart count
// cartCount.innerText = '0';




let products = [
    {
        name: 'Python',
        tag: 'Python',
        price: 150,
        inCart: 0
    },
    {
        name: 'Java',
        tag: 'Java',
        price: 150,
        inCart: 0
    }
];



// let carts = document.querySelectorAll('.add-cart')
// console.log(carts.length)

// for (let i=0; i < carts.length; i++){
//     carts[i].addEventListener('click',() => {
//         cartNumbers(products[i]);

//     })
// }

const cart = [];

document.querySelectorAll(".add-cart").forEach(button => {
  button.addEventListener("click", () => {
    const itemId = button.dataset.itemId;
    const item = { id: itemId };
    cart.push(item);
console.log(cart)

    Id = parseInt(itemId)
    cartNumbers(products[Id],Id);
    button.classList.add('clicked')
   

  });
});



function onLoadCartNumbers(){
    let productNumbers = localStorage.getItem('cartNumbers');
    let clickedButton = localStorage.getItem('clickedButton')
   
    
    if(productNumbers){
        document.querySelector('.cart-count').textContent = productNumbers;
        
    }
    


}

function cartNumbers(products,Id) {
    let clickedButton = document.querySelector('.clicked')
    console.log("The product clicked is", products);
    console.log(Id)
    
    let productNumbers = localStorage.getItem('cartNumbers');

    productNumbers = parseInt(productNumbers);

    if(clickedButton){
        
        console.log(clickedButton)
    }
    
    else{
        if(productNumbers){
            localStorage.setItem('cartNumbers', productNumbers + 1);
          
            localStorage.setItem('clickedButton', Id);
            document.querySelector('.cart-count').textContent = productNumbers + 1;
        } 
        else {
            localStorage.setItem('cartNumbers', 1);
            document.querySelector('.cart-count').textContent = 1;
        }
    }
   
}

onLoadCartNumbers();


// end of add to cart