var editButton = document.querySelectorAll('#edit');

var subEditButton = document.querySelectorAll('#edit-sub');


// category edit button click handler
editButton.forEach((element) => {
    element.addEventListener('click', (e) => {
        var slug = e.target.getAttribute('data-slug');
      fetch(`/admin/catagory/${slug}/json`)
      .then((res)=>res.json())
      .then(data => {
        // Access the form and its input fields
        var form = document.getElementById('category-form');
        var nameInput = form.querySelector('input[name="name"]');
        var slugInput = form.querySelector('input[name="slug"]');
        var submitButton = form.querySelector('#submit');
        // Set the data into the form fields
        nameInput.value = data.category.name;
        slugInput.value = data.category.slug;
        submitButton.innerHTML = "Update"
        form.action = `category/${slug}/update`
    })
      .catch((err)=>console.log(err))

      //  giving the value to the form
    });
  });


  // sub edit button click handler
subEditButton.forEach((element)=>{
  element.addEventListener('click', (e)=>{
    const form = document.getElementById('input[name ="title"')
    conn
    subcat_slug = e.target.getAttribute("data-slug")
    fetch(`/admin/subcategory/${subcat_slug}/json`)
    .then(response=>response.json())
    .then(data=>console.log(data));
  })
})

