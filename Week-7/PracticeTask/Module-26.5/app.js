const allProducts = document.getElementById('products');
const spinner = document.getElementById('spinner');
const noData = document.getElementById('nodata');
const allCategory = document.getElementById('category');

const loadCategories = async () => {
  try {
    const response = await fetch(
      'https://fakestoreapi.com/products/categories'
    );
    const categories = await response.json();
    displayCategories(categories);
  } catch (error) {
    console.error('Error fetching categories:', error);
  }
};

const displayCategories = (categories) => {
  categories.forEach((category) => {
    const buttonElement = createButtonElement(category);
    allCategory.appendChild(buttonElement);
  });
};

const createButtonElement = (category) => {
  const buttonElement = document.createElement('btn');
  buttonElement.classList.add('button','btn', 'btn-info','m-2');
  buttonElement.textContent = category;
  buttonElement.addEventListener('click', () => {
    loadProducts(category);
  });
  return buttonElement;
};

const loadProducts = async (category) => {
  try {
    allProducts.innerHTML = '';
    spinner.style.display = 'block';
    noData.style.display = 'none';

    let url = 'https://fakestoreapi.com/products';
    if (category) {
      url += `/category/${category}`;
    }

    const response = await fetch(url);
    const data = await response.json();

    if (data?.length > 0) {
      spinner.style.display = 'none';
      displayProducts(data);
    } else {
      noData.style.display = 'block';
    }
  } catch (error) {
    console.error('Error loading products:', error);
  }
};

const displayProducts = (products) => {
  const parent = allProducts;

  products.forEach((item) => {
    const div = createProductCard(item);
    parent.appendChild(div);
  });
};

const createProductCard = (item) => {
  const div = document.createElement('div');
  div.classList.add(
    'col-lg-3',
    'col-md-6',
    'mb-4',
    'mb-lg-0',
    'card-container'
  );
  div.innerHTML = `
    <div class="card rounded shadow-sm border-0">
        <div class="card-body p-4">
            <img class="card-img" src=${
              item.image
            } alt="" class="img-fluid d-block mx-auto mb-5">
            <h5>${item.title.slice(0, 15)}..</h5>
            <p class="font-bold">Price: ${item.price}$</p>
            <p>Category: ${item.category}</p>
            <p>Rating: ${item.rating?.rate}</p>
            <a target="_blank" href="cardDetails.html?cardId=${item.id}" class="btn btn-info">Details</a>
        </div>
    </div>
  `;
  return div;
};


loadProducts();
loadCategories();
