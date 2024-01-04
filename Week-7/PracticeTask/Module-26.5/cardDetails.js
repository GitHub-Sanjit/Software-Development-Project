const getParams = async () => {
  try {
    const param = new URLSearchParams(window.location.search).get('cardId');
    const response = await fetch(`https://fakestoreapi.com/products/${param}`);
    const data = await response.json();
    displayCardDetails(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

const displayCardDetails = (post) => {
  const parent = document.getElementById('product-details');
  const div = document.createElement('div');
  div.classList.add('container', 'm-10');
  div.innerHTML = `
    <div class="row align-items-center m-auto">
      <div class="col-lg-6 m-15">
        <img class="cardDetails-img" src=${post.image} alt="">
      </div>
      <div class="col-lg-6 m-15">
        <div class="card-body">
          <div class="space-y-2">
            <h2 class="card-title text-3xl font-weight-bold">${post.title}</h2>
            <p class="card-text">Price: ${post.price}</p>
            <p>Category: ${post.category}</p>
            <p>Rating: ${post.rating?.rate}</p>
            <p>Description: ${post.description}</p>
          </div>
          <a target="_blank" href="index.html?cardId=${post.id}" class="btn btn-info">Buy Now</a>
        </div>
      </div>
    </div>
  `;
  parent.appendChild(div);
};

getParams();
