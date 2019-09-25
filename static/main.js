// Event Listener for the Add Label Badge which opens the modal
function addLabelEventListener(event) {
  const div = document.getElementById('modal-labels-set');
  div.innerHTML = `<p>Existing labels: </p>`;
  // Get all the labels which are getting used on the current page (Or atleast those, which are on the top of the page) and display them in the modal
  const childs = event.target.parentElement.parentElement.children[0].children;
  for (let label of childs) {
    div.innerHTML += `${label.outerHTML} `;
  };
}
document.getElementById('addlabel')
  .addEventListener('click', addLabelEventListener);

// Function that gets called after clicking Add Label in the new Label modal
function addNewLabel() {
  const labelName = document.getElementById('newLabelInput')
    .value;
  const labelclass = labelName.replace(" ", "")
    .toLowerCase();
  const div = document.getElementById('labelselect');
  // Get the next colour
  const colour = colourArray[colourIndex];
  colourIndex += 1;
  if (colourIndex == colourArray.length) colourIndex = 0; // start at the beginning of the colour array
  // make html and add to the top of the page
  const html = `<span class="badge ${labelclass}" id="${labelclass}-label" draggable="true" ondragstart="drag(event)" style="background-color: ${palette.get(colour, '700')};color:${palette.getText(colour, '500', 'Secondary')}">${labelName}</span>`;
  div.innerHTML += html;
  // clear input
  document.getElementById('newLabelInput')
    .value = '';
  // close modal
  document.getElementById('cancelButton')
    .click();
}
// send patch request to the server with keyword in path and category in body which should get associated
async function updateKeyword(keyword, category) {
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

// Base code for drag and drop from: https://stackoverflow.com/questions/13007582/html5-drag-and-copy
// Modified to fit my usage
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
  nodeCopy.removeAttribute('draggable'); // We dont want the set label to be draggable
  nodeCopy.removeEventListener('dragstart', drag); // So we also need to remove the drag event listners!
  const keyword = ev.target.innerText;
  const category = nodeCopy.innerText;
  ev.target.parentNode.replaceChild(nodeCopy, ev.target); // Replace keyword with label
  updateKeyword(keyword, category); // send request to server
}

// Function that gets called if you click on the ... Badge next to the labels
function showKeywords(ev) {
  // check if its collapsed or not
  const collapsed = ev.path[2].cells[1].children[0].dataset.collapsed;
  if (collapsed === 'true') {
    ev.path[2].cells[1].children[0].dataset.collapsed = false;
    const id = ev.path[2].cells[1].children[0].dataset.id;
    articles.forEach((article) => { // iterate through the current articles
      let html = '';
      if (article.id === id) { // we found our article
        article.keywords.forEach((keyword) => { // iterate through keywords and set them 
          html += `<div class="inline keyword" ondrop="drop(event)" ondragover="allowDrop(event)" ondblclick="removeKeyword(event)">${keyword}</div>`;
        });
        ev.target.parentElement.innerHTML += html; // html is the string with all our keywords
      }
    });
  } else {
    // set as collapsed
    ev.path[2].cells[1].children[0].dataset.collapsed = true;
    let remove = [];
    // find all keywords
    for (let item of ev.target.parentElement.children) {
      if (item.classList.contains('keyword')) remove.push(item);
    }
    // remove all found keywords
    for (let item of remove) {
      item.remove();
    }
  }

}
// gets called on dblclick on a keyword
function removeKeyword(ev) {
  const keyword = ev.target.innerText; //keyword to be removed
  const id = ev.path[2].cells[1].children[0].dataset.id; // id of the article
  // send patch request to server with id as path variable and the keyword in the body
  fetch(`http://localhost:5000/api/v1/article/${id}`, {
    body: JSON.stringify({
      "keyword": keyword
    }),
    method: "PATCH",
    headers: {
      'Content-Type': 'application/json'
    }
  });
  // remove keyword from frontend
  ev.target.remove();
}
// Function that gets called by the pagination buttons with either + or - 20
function loadArticles(i) {
  if (index + i > 0) { // if we get < 0, we want to show negative amount of articles? tf? dont do that >:(
    document.getElementById('articletable')
      .innerHTML = ''; // clear article table
    document.getElementById('labelselect')
      .innerHTML = '<span class="badge all" id="all-label" draggable="true" ondragstart="drag(event)">All</span>'; // remove all labels besides the all label
    index += i; // add the indices
    load(); // actually do the loading process
  }
}
// Used to display categories / labels more nicely
const firstLetterToUpperCase = string => string[0].toUpperCase() + string.substring(1);
// Colour palette used by google material colour palette.
const colourArray = ['Red', 'Pink', 'Purple', 'Deep Purple', 'Indigo', 'Blue', 'Light Blue', 'Cyan', 'Teal', 'Green', 'Light Green', 'Lime', 'Yellow', 'Amber', 'Orange', 'Deep Orange', 'Brown', 'Grey', 'Blue Grey', 'Black', 'White'];
let colourIndex = 0;
let articles;
let index = 20;
const load = async () => {
  // fetch articles from api
  const url = `http://localhost:5000/api/v1/articles/${index}`;
  let categories = [];
  const fetchAsyncA = async () => {
    articles = await (await fetch(url))
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
        .innerHTML = `<a href="${article.url}" data-id="${article.id}" data-collapsed="true" >${article.title}</a>`;
      const keywords = row.insertCell(2);
      keywords.className += (keywords.className ? ' ' : '') + 'keywords';

      let html = "";
      article.categories.forEach((category) => {
        categories.push(category);
        const colour = colourCategories[category];
        html += `<span class="badge" style="background-color: ${palette.get(colour, '700')};color:${palette.getText(colour, '500', 'Secondary')};font-size:87%;">${firstLetterToUpperCase(category)}</span>`;
      });
      if (article.categories.length < 1) { // if we have labels for that article, dont show the keywords
        article.keywords.forEach((keyword) => {
          html += `<div class="inline keyword" ondrop="drop(event)" ondragover="allowDrop(event)" ondblclick="removeKeyword(event)">${keyword}</div>`;
        });
      } else if (article.keywords.length > 0) { // if we still have some keywords left over, give the option to show them
        html += `<span class="badge" style="background-color: #424242;color:#fff;font-size:87%;" onclick="showKeywords(event)";>...</span>`;
      }

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
    // only make the pagination visible if our table got built or else it looks really ugly while loading:D
    document.getElementById('pagination')
      .style.visibility = 'visible';
  }
  fetchAsyncA();
}
// DAVAI DAVAI
load();