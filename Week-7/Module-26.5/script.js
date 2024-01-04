document.addEventListener('DOMContentLoaded', () => {
  const categoryList = document.getElementById('categoryList');
  const productList = document.getElementById('productList');
  const productDetails = document.getElementById('productDetails');
  const details = document.getElementById('details');

  // Fetch categories
  fetch('https://fakestoreapi.com/products/categories')
    .then((response) => response.json())
    .then((categories) => {
      categories.forEach((category) => {
        const li = document.createElement('li');
        li.textContent = category;
        categoryList.appendChild(li);
      });
    });

  // Fetch all products
  fetch('https://fakestoreapi.com/products')
    .then((response) => response.json())
    .then((products) => {
      products.forEach((product) => {
        const li = document.createElement('li');
        li.textContent = product.title;
        li.classList.add('product');

        li.addEventListener('click', () => showProductDetails(product));

        productList.appendChild(li);
      });
    });

  function showProductDetails(product) {
    details.innerHTML = `
            <strong>Title:</strong> ${product.title}<br>
            <strong>Category:</strong> ${product.category}<br>
            <strong>Price:</strong> $${product.price}<br>
            <strong>Description:</strong> ${product.description}<br>
            <img src="${product.image}" alt="${product.title}" width="200">
        `;
    productDetails.style.display = 'block';
  }
});
