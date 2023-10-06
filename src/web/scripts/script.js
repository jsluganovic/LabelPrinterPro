/* ----- inputs ----- */
const codeFormInput = document.querySelector('.code-form__input')
const textFormInput = document.querySelector('.text-form__input')

/* ----- buttons ----- */
const codeFormButton = document.querySelector('.code-form__button')
const textFormButton = document.querySelector('.text-form__button')
const outputButtonReset = document.querySelector('.output-button__reset')
const outputButtonDownload = document.querySelector('.output-button__download')

/* ----- Input type radio ----- */
const formSvgQrcode = document.querySelector('.form-svg__qrcode')
const formSvgBarcode = document.querySelector('.form-svg__barcode')

/* ----- img ----- */
const img = document.querySelector('.output-code__img')
const outputText = document.querySelector('.output-text')

let myDiv = document.createElement('div')


codeFormButton.addEventListener('click', (e) => {
    e.preventDefault()

    console.log('qr & barcode')
    if (formSvgQrcode.checked) {
        let codeInputValue = codeFormInput.value.trim() 

        img.src = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${codeInputValue}`
    } else {
        JsBarcode("#barcode", codeFormInput.value);
    }
})

textFormButton.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('text')
    let textInputValue = textFormInput.value
    myDiv.textContent = textInputValue
    outputText.appendChild(myDiv)
})

outputButtonReset.addEventListener('click', (e) => {
    img.src = ``
    JsBarcode("#barcode", '11', {
        format: "pharmacode",
        lineColor: "#fff",
        width: 4,
        height: 40,
        displayValue: false
      })

    outputText.removeChild(myDiv)
})

outputButtonDownload.addEventListener('click', () => {
    html2canvas(document.querySelector('.output'))
        .then(canvas => {
            const url = canvas.toDataURL('image/svg')
            const a = document.createElement('a')
            a.setAttribute('download', 'imageName.svg')
            a.setAttribute('href', url)
            a.click()
        })
})

