console.log("Csatlakozás sikeres")
let delete_buttons = document.querySelectorAll(".delete-item")

function delete_item_from_cart(event) {
    if (event.target.closest("tr")) {
        const itemId = event.target.closest("tr").id
        console.log(itemId)

        fetch(`/cart/delete/${itemId}/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                event.target.closest("tr").remove()
                
                const newTotal = data.new_total
                document.getElementById('cart-total').innerText = formatPrice(newTotal)

                checkEmptyCart();
            } else {
                alert("Hiba: " + data.error)
            }
        })
    }
}

function getCookie(name) {
    let cookieValue = null
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';')
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim()
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break
            }
        }
    }
    return cookieValue
}
function checkEmptyCart() {
    const items = document.querySelectorAll('.cart-items')
    const emptyRow = document.querySelector('.cart-empty-row')
    const table = document.querySelector('.cart-list')

    if (!table) return

    if (items.length === 0 && !emptyRow) {
        table.insertAdjacentHTML(
            'beforeend',
            `
            <tr class="cart-empty-row">
                <td colspan="6">
                    <div class="cart-empty">
                        <p class="cart-empty-title">A kosár üres</p>
                    </div>
                </td>
            </tr>
            `
        )

        const totalEl = document.getElementById('cart-total')
        if (totalEl) {
            totalEl.textContent = '0'
        }
    }
}

function formatPrice(value) {
    const num = Number(value) || 0
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
}

const totalEl = document.getElementById('cart-total')
if (totalEl && totalEl.textContent.trim() !== "" && totalEl.textContent.trim() !== "0") {
    totalEl.textContent = formatPrice(totalEl.textContent.trim())
}

delete_buttons.forEach(del_but => {
    del_but.addEventListener("click", delete_item_from_cart)
})
