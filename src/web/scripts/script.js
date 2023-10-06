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

       
        fetch('http://127.0.0.1:5000/gqrcode', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                qrcode_data: codeInputValue,
                reqNumber: "123123" 
            }),
           
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            img.src = `https://rff7hjr5-5000.euw.devtunnels.ms/uqrcode/${data.req_number}`
        })
        .catch(error => console.error(error))
    } else {
       // JsBarcode("#barcode", codeFormInput.value);
        let codeInputValue = codeFormInput.value.trim() 

       
        fetch('http://127.0.0.1:5000/gbarcode', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                bcode_data: codeInputValue,
                req_number: "123123" 
            }),
           
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            img.src = `https://rff7hjr5-5000.euw.devtunnels.ms/ubarcode/${data.req_number}`
        })
        .catch(error => console.error(error))
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
            const url = canvas.toDataURL('image/png')
            const a = document.createElement('a')
            a.setAttribute('download', 'imageName.png')
            a.setAttribute('href', url)
            a.click()
        })
})

