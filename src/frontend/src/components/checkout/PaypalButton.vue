<template>
    <div class="checkout-button-container">
        <button class="pay-button" :class="{ close: isPayPalButtonVisible }" @click="toggleButton">
            {{ buttonText }}
        </button>
        <div id="paypal-button-container" v-if="isPayPalButtonVisible"></div>
    </div>
</template>

<script>
import env from "../../../env";
export default {
    name: "paypal-button",
    props: {
        amount: {
            type: Number,
            default: 100000,
        },
        message: {
            type: String,
            default: "Nothing",
        },
        paypalCurrency: {
            type: String,
            default: "USD",
        },
    },
    data() {
        return {
            isPayPalButtonVisible: false,
            buttonText: "Pay Now",
        };
    },
    methods: {
        toggleButton() {
            if (this.isPayPalButtonVisible === false) {
                this.isPayPalButtonVisible = true;
                this.buttonText = "Cancel";
                const script = document.createElement("script");
                script.onload = this.initializePayPalButton;
                script.src = `https://www.paypal.com/sdk/js?client-id=${env.PAYPAL_CLIENT_ID}`;
                document.head.appendChild(script);
            } else {
                this.isPayPalButtonVisible = false;
                this.buttonText = "Pay Now";
            }
        },

        togglePayPalButton() {
            if (this.isPayPalButtonVisible === false) {
                this.isPayPalButtonVisible = true;
                this.buttonText = "Cancel";
            } else {
                this.isPayPalButtonVisible = false;
                this.buttonText = "Pay Now";
            }
        },
        initializePayPalButton() {
            window.paypal
                .Buttons({
                    createOrder: (data, actions) => {
                        return actions.order.create({
                            purchase_units: [
                                {
                                    description: this.message,
                                    amount: {
                                        currency_code: this.paypalCurrency,
                                        value: this.amount,
                                    },
                                },
                            ],
                        });
                    },
                    onApprove: async (data, actions) => {
                        const order = await actions.order.capture();
                        this.$emit("execute-transaction");
                        console.log(order);
                        this.togglePayPalButton();
                    },
                    onError: (err) => {
                        console.log(err);
                        this.togglePayPalButton();
                    },
                })
                .render("#paypal-button-container");
        },
    },
};
</script>

<style scoped lang="scss">
.checkout-button-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    .pay-button {
        display: inline-block;
        padding: 10px 20px;
        background-color: var(--cs-color-button);
        color: white;
        text-align: center;
        font-size: 16px;
        border: none;
        cursor: pointer;
        border-radius: 4px;
        transition: background-color 0.3s, transform 0.3s;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    .pay-button.close {
        background-color: #f44336;
    }

    .pay-button:hover {
        background-color: var(--cs-color-button-hover);
        transform: scale(1.05);
    }

    .pay-button.close:hover {
        background-color: #e53935;
    }

    .pay-button i {
        margin-right: 5px;
    }
}
</style>
