$(document).ready(loadCupcakes)

async function loadCupcakes(){
    const response = await axios.get('/api/cupcakes')
    const cupcakes = response.data.cupcakes
    for (const cupcake of cupcakes) {
        const newLI = $('<li></li>')
        const newDiv = $('<div></div>')
        const cupcakeImage = $(`<img src="${cupcake.image}">`)
        const cupcakeSize = $(`<p>Size: ${cupcake.size}</p>`)
        const cupcakeFlavor = $(`<p>Flavor: ${cupcake.flavor}</p>`)
        const cupcakeRating = $(`<p>Rating: ${cupcake.rating}</p>`)
        newDiv.append(cupcakeImage)
        newDiv.append(cupcakeFlavor)
        newDiv.append(cupcakeSize)
        newDiv.append(cupcakeRating)
        newLI.append(newDiv)
        $("ul").append(newLI)
        $("ul").append('<br>')
    }
}

const $ratingVal = $('#rating-val')
$ratingVal.text($('#rating').val())
$('#rating').on('input', function(){
    let value = $(this).val()
    $ratingVal.text(value)
})

$('form').on('submit', async function(event){
    event.preventDefault()
    const flavor = $('#flavor').val()
    const size = $('#size').val()
    const rating = $('#rating').val()
    const image = $('#image').val()
    const response = await axios({
      url: '/api/cupcakes', 
      method: 'POST',
      data: {flavor, size, rating, image}})
    const cupcake = response.data.cupcake
    const newLI = $('<li></li>')
    const newDiv = $('<div></div>')
    const cupcakeImage = $(`<img src="${cupcake.image}">`)
    const cupcakeSize = $(`<p>Size: ${cupcake.size}</p>`)
    const cupcakeFlavor = $(`<p>Flavor: ${cupcake.flavor}</p>`)
    const cupcakeRating = $(`<p>Rating: ${cupcake.rating}</p>`)
    newDiv.append(cupcakeImage)
    newDiv.append(cupcakeFlavor)
    newDiv.append(cupcakeSize)
    newDiv.append(cupcakeRating)
    newLI.append(newDiv)
    $("ul").append(newLI)
    $("ul").append('<br>')
})

async function addCupcake(){}