let num = 0
window.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('my_form');
  const fileInput = document.getElementById('file-upload')
    console.log('DOMContentLoaded')
    console.log('form is ' + form)
  form.addEventListener('submit', event => {
    num += 1
    event.preventDefault()
    console.log(event)
    const input = document.getElementById('voice-form');
    console.log('text submit!!')
    console.log("value of input.value: " + input.value)
    const new_data = {
      has_pdf: false,
      pdf_name: null,
      text: input.value
    }
    const name = 'storedItem' + num
    localStorage.setItem(name, JSON.stringify(new_data))
    console.log(name + ": " + localStorage.getItem(name))
    input.value = ''
    //HOW TO MAKE API CALL FROM HERE
    // fetch('/store', {
    //   Method: 'POST',
    //   Headers: {
    //     Accept: 'application.json',
    //     'Content-Type': 'application/json'
    //   },
    // })
  });
  fileInput.onchange = () => {
    num += 1
  console.log('FILE UPLOAD')
  //I should parse the file here and send it ->
const selectedFile = fileInput.files[0];
console.log(selectedFile);
const new_data = {
      has_pdf: false,
      pdf_name: selectedFile.name,
      text: null
    }
    const name = 'storedItem' + num
    localStorage.setItem(name, JSON.stringify(new_data))
    console.log(name + ' is ' + localStorage.getItem(name))
}
});