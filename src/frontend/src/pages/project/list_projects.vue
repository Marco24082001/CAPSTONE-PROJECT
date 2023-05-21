<template>
    <div class="container">
        <div class="products">
            <div class="product">
                <div class="image">
                    <img src="@/assets/product_img/earphone.png" alt="" />
                </div>
                <div class="namePrice">
                    <h3>earphone</h3>
                    <span>$ 15.99</span>
                </div>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p>
                <div class="stars">
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-regular fa-star"></i>
                </div>
                <div class="bay">
                    <button>bay now</button>
                </div>
            </div>

            <div class="product">
                <div class="image">
                    <img src="@/assets/product_img/iphone2.png" alt="" />
                </div>
                <div class="namePrice">
                    <h3>iphone</h3>
                    <span>$ 120.99</span>
                </div>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                <div class="stars">
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-regular fa-star"></i>
                </div>
                <div class="bay">
                    <button>bay now</button>
                </div>
            </div>

            <div class="product">
                <div class="image">
                    <img src="@/assets/product_img/laptop.png" alt="" />
                </div>
                <div class="namePrice">
                    <h3>laptop</h3>
                    <span>$ 150.99</span>
                </div>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                <div class="stars">
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                </div>
                <div class="bay">
                    <button>bay now</button>
                </div>
            </div>

            <div class="product">
                <div class="image">
                    <img src="@/assets/product_img/watch3.png" alt="" />
                </div>
                <div class="namePrice">
                    <h3>watch</h3>
                    <span>$ 20.99</span>
                </div>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                <div class="stars">
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-regular fa-star"></i>
                </div>
                <div class="bay">
                    <button>bay now</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "List-Projects",
};
</script>

<style scoped lang="scss">
:root{
    --bodyBack: #ffeaed;
    --textColor: #1b2741;
    --starColor: #f67034;
    --sectionBack: #f7f6f9;
}

.container{
    width: 100vw;
    display: flex;
    flex-direction: column;
    // justify-content: space-around;
}

.products{
    width: 100%;
    align-self: center;
    height: 30%;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 3rem;
}
.product{
    position: relative;
    background-color: var(--sectionBack);
    width: 350px;
    height: 300px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, .3);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 20px 20px 40px;
    border-radius: 10px;
    transition: .3s;
}
.product:hover{
    transform: translateY(-15px);
    box-shadow: 0 5px 10px rgba(0, 0, 0, .2);
}
.image{
    width:100%;
    height: 60%;
    display: grid;
    place-content: center;
}
.image img{
    width: 240px;
}
.namePrice{
    width: 100%;
    display: flex;
    justify-content: space-between;
}
.namePrice h3{
    font-size: 2em;
    text-transform: capitalize;
    color: var(--textColor);
}
.namePrice span{
    font-size: 1.5em;
    color: var(--starColor);
}
.product p{
    font-size: 18px;
    line-height: 25px;
}
.stars svg{
    font-size: 1.3em;
    color: var(--starColor);
}
.bay{
    position: absolute;
    bottom: 20px;
    right: 20px;
}
.bay button{
    padding: 10px 20px;
    border-radius: 7px;
    border: none;
    background-color: var(--textColor);
    color: var(--sectionBack);
    font-size: 18px;
    text-transform: capitalize;
    cursor: pointer;
    transition: .5s;
}
.bay button:hover{
    transform: scale(1.1);
}
</style>
