// https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=
// https://rff7hjr5-5000.euw.devtunnels.ms/process

if (!codeInputValue || previousValue === codeInputValue) return
previousValue = codeInputValue

img.addEventListener('load', () => {
    codeFormButton.innerHTML = 'Generieren'
})

codeFormButton.innerHTML = 'Genereting ...'

if (!textInputValue || previousValue2 === textInputValue) return
previousValue2 = textInputValue