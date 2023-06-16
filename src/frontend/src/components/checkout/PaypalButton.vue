<template>
    <div>
        <button @click="paymethod">tinh tien</button>
        <div ref="paypal"></div>
    </div>
</template>

<script>
import env from "../../../env";
// import env from "env";
export default {
    name: "paypal-button",
    props: {
        amount: Number,
        message: String,
    },
    data() {
        return {
            paypalCurrency: "",
            paidFor: false,
            loaded: false,
        };
    },
    created() {
        const script = document.createElement("script");
        script.src = `https://www.paypal.com/sdk/js?client-id=${env.PAYPAL_CLIENT_ID}`;
        document.body.appendChild(script);
    },
    methods: {
        paymethod: function () {
            this.setLoadPayment();
        },
        setLoadPayment: function () {
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
                        this.paidFor = true;
                        console.log(order);
                    },
                    onError: (err) => {
                        console.log(err);
                    },
                })
                .render(this.$refs.paypal);
        },
    },
};
</script>
