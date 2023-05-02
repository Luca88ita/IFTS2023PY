let cart = [];

validateInput = (input) =>{
  let validInput = input.trim();
  return (validInput.length>0);
}

addProduct = () => {
  event.preventDefault();
  if (!validateInput(prodottoTXT.value)) return;
  let filtred = cart.filter(x => x.nome == prodottoTXT.value);
  if (filtred.length>0){
    increaseQuantity(filtred);
  }else{
    addNewProduct();
  }
  stampa();
  
}

addNewProduct = () =>{
  let product = {
    nome: prodottoTXT.value,
    prezzo: 10,
    quantita: 1,
  } 
  cart.push(product);
};

increaseQuantity = (filtred) =>{
  filtred[0].quantita++;
};

removeProduct = (toBeRemoved) => {
  idx = -1;
  for(let i = 0; i<cart.length;i++){
    if (cart[i].nome == toBeRemoved) idx = i;
  }
  //index = cart.indexOf(item);
  cart.splice(idx,1);
  //let button = this;
  let button = event.target;
  let li = button.parentNode;
  li.remove();
  stampa();
};

addPiece = (toBeIncreased) => {
  for(let i = 0; i<cart.length;i++){
    if (cart[i].nome == toBeIncreased) cart[i].quantita++;
  }
  stampa();
}

removePiece = (toBeDecreased) =>{
  for(let i = 0; i<cart.length;i++){
    if (cart[i].nome == toBeDecreased) cart[i].quantita--;
    if (cart[i].quantita <=0)removeProduct(cart[i]);
  }
  stampa();
}

stampa = () => {
  cartUL.innerHTML = '';
  for (let product of cart) {
    let item = product.nome;
    cartUL.innerHTML += `
    <li>
      ${item} - ${product.quantita}
      <button onclick="addPiece('${item}')">+</button>
      <button onclick="removePiece('${item}')">-</button>
      <button onclick="removeProduct('${item}')">X</button>
    </li>
    `;
  }
};


/*stampa = ( product ) => {
  let item = product.nome;
  let newLi = document.createElement("li")
  newLi.innerHTML += `
    ${item} - ${product.quantita}
    <button onclick="addPiece('${item}')">+</button>
    <button onclick="removePiece('${item}')">-</button>
    <button onclick="removeProduct('${item}')">X</button>
  `;
  cartUl.appendChild(newLi);
};*/

save = () =>{
  cartJSONString = JSON.stringify(cart)
  localStorage.setItem(
    "cart",cartJSONString
  )
}
load = () =>{
  stringJSON = localStorage.getItem("cart");
  oggetto = JSON.parse(stringJSON);
  if(oggetto){
    cart = oggetto;
  }
  stampa();
}