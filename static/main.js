function addLabelEventListener(event) {
  const div = document.getElementById('modal-labels-set');
  div.innerHTML = `<p>Existing labels: </p>`;
  const childs = event.target.parentElement.parentElement.children[0].children;
  for (let label of childs) {
    div.innerHTML += `${label.outerHTML} `;
  };
}
document.getElementById('addlabel')
  .addEventListener('click', addLabelEventListener);

function addNewLabel() {
  const labelName = document.getElementById('newLabelInput')
    .value;
  const labelclass = labelName.replace(" ", "")
    .toLowerCase();
  const div = document.getElementById('labelselect');
  const html = `<span class="badge ${labelclass} standard" id="${labelclass}-label" draggable="true" ondragstart="drag(event)">${labelName}</span>`;
  div.innerHTML += html;
  document.getElementById('newLabelInput')
    .value = '';
  document.getElementById('cancelButton')
    .click();
}

function updateKeyword(keyword, category) {
  fetch(`http://localhost:5000/api/v1/categories/${keyword}`, {
    body: JSON.stringify({
      "category": category
    }),
    method: "PATCH",
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then((response) => {
      console.log(response);
    });
}
// DRAG AND DROP CODE TAKEN FROM: https://stackoverflow.com/questions/13007582/html5-drag-and-copy
function allowDrop(ev) {
  /* The default handling is to not allow dropping elements. */
  /* Here we allow it by preventing the default behaviour. */
  ev.preventDefault();
}

function drag(ev) {
  /* Here is specified what should be dragged. */
  /* This data will be dropped at the place where the mouse button is released */
  /* Here, we want to drag the element itself, so we set it's ID. */
  ev.dataTransfer.setData('text/html', ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData('text/html');
  /* If you use DOM manipulation functions, their default behaviour it not to 
     copy but to alter and move elements. By appending a ".cloneNode(true)", 
     you will not move the original element, but create a copy. */
  var nodeCopy = document.getElementById(data)
    .cloneNode(true);
  nodeCopy.removeAttribute('id'); /* We cannot use the same ID */
  nodeCopy.addEventListener('dblclick', remove);
  const keyword = ev.target.innerText;
  const category = nodeCopy.innerText;
  ev.target.innerHTML = "";
  ev.target.appendChild(nodeCopy);
  updateKeyword(keyword, category);
}

function remove(ev) {
  ev.target.remove()
}

function removeKeyword(ev) {
  const keyword = ev.target.innerText;
  const id = ev.path[2].cells[1].children[0].dataset.id;
  fetch(`http://localhost:5000/api/v1/article/${id}`, {
    body: JSON.stringify({
      "keyword": keyword
    }),
    method: "PATCH",
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then((response) => {
      console.log(response);
    });
  ev.target.remove();
}
const firstLetterToUpperCase = string => string[0].toUpperCase() + string.substring(1);
const colourArray = ['Red', 'Pink', 'Purple', 'Deep Purple', 'Indigo', 'Blue', 'Light Blue', 'Cyan', 'Teal', 'Green', 'Light Green', 'Lime', 'Yellow', 'Amber', 'Orange', 'Deep Orange', 'Brown', 'Grey', 'Blue Grey', 'Black', 'White'];
const random = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
(async () => {
  const url = 'http://localhost:5000/api/v1/articles'
  let categories = [];
  const fetchAsyncA = async () => {
    const articles = await (await fetch(url))
      .json();
    // Step 0: Iterate through all articles and collect the categories. Then give every category a nice color
    const colourCategories = {};
    let colourIndex = 0;
    articles.forEach((article) => {
      article.categories.forEach((category) => {
        if (colourCategories[category] === undefined) {
          colourCategories[category] = colourArray[colourIndex];
          colourIndex += 1;
          if (colourIndex === colourArray.length) colourIndex = 0;
        }
      });
    });
    // Step 1: Fill articles into table
    const table = document.getElementById('articletable');
    let counter = articles.length;
    articles.forEach((article) => {
      const row = table.insertRow(0);
      const index = row.insertCell(0)
        .innerHTML = counter;
      const title = row.insertCell(1)
        .innerHTML = `<a href="${article.url}" data-id="${article.id}">${article.title}</a>`;
      const keywords = row.insertCell(2);
      let html = "";
      article.categories.forEach((category) => {
        categories.push(category);
        const colour = colourCategories[category];
        html += `<span class="badge" style="background-color: ${palette.get(colour, '700')};color:${palette.getText(colour, '500', 'Secondary')};font-size:87%;">${firstLetterToUpperCase(category)}</span>`;
      });
      article.keywords.forEach((keyword) => {
        html += `<div class="inline keyword" ondrop="drop(event)" ondragover="allowDrop(event)" ondblclick="removeKeyword(event)">${keyword}</div>`;
      });
      keywords.innerHTML = html;
      counter -= 1;
    });
    // Step 2: Show used categories at the top
    categories = categories.filter((e, i) => categories.indexOf(e) === i); // Kill duplicates
    const labels = document.getElementById('labelselect');
    categories.forEach((category) => {
      const colour = colourCategories[category];
      const html = `<span class="badge" id="${category}" style="background-color: ${palette.get(colour, '700')}; color:${palette.getText(colour, '500', 'Secondary')}; font-size:87%;" draggable="true" ondragstart="drag(event)">${firstLetterToUpperCase(category)}</span>`
      labels.innerHTML += html;
    });
  }
  fetchAsyncA();
})();