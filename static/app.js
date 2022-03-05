


// get a cupcake

function getOneCupcake(cupcake) {
  return `
    <div data-cupcake-id=${cupcake.id}>
        ${cupcake.flavor} <br> 
        ${cupcake.size} <br> 
        ${cupcake.rating} <br>
        <button class="delete-button">Delete</button>
        <img class="Cupcake-img"
        src="${cupcake.image}"
        alt="${cupcake.flavor}">
    </div>
  `;
}


/** put initial cupcakes on page. */
$(allCupcakes);

async function allCupcakes() {
  const response = await axios.get("/api/cupcakes");

  for (let cupcake of response.data.cupcakes) {
    let newCupcake = getOneCupcake(cupcake);
    $("#cupcakes-list").append(newCupcake);
  }
}


// deletes a cupcake
$('.delete-cupcake').click(deleteCupcake)

async function deleteCupcake(evt) {
  evt.preventDefault()
  const id = $(this).data('id')
  alert(id)
  await axios.delete(`/api/cupcakes/${id}`)
  $(this).parent().remove()
}