<template>
    <div class="container">
        <div class="card-projects">
            <div class="card-project">
                <div class="image">
                    <img src="@/assets/project_img/project-0.jpg" alt="" />
                </div>
                <div class="namePrice">
                    <h3>Chung tay hỗ trợ học</h3>
                    <!-- <span>$ 15.99</span> -->
                </div>
                <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
            </div>

            <div class="card-project">
                <div class="image">
                    <img src="@/assets/project_img/project-2.png" alt="" />
                </div>
                <div class="namePrice">
                    <h3>Chung tay hỗ trợ học</h3>
                    <!-- <span>$ 15.99</span> -->
                </div>
                <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
            </div>

            <div class="card-project">
                <div class="image">
                    <img src="@/assets/project_img/project-3.jpg" alt="" />
                </div>
                <div class="namePrice">
                    <h3>Chung tay hỗ trợ học</h3>
                    <!-- <span>$ 15.99</span> -->
                </div>
                <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
            </div>

            <div class="card-project">
                <div class="image">
                    <img src="@/assets/project_img/project-4.png" alt="" />
                </div>
                <div class="namePrice">
                    <h3>Chung tay hỗ trợ học</h3>
                    <!-- <span>$ 15.99</span> -->
                </div>
                <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
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
:root {
    --bodyBack: #ffeaed;
    --textColor: #1b2741;
    --starColor: #f67034;
    --sectionBack: #f7f6f9;
}

.container {
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    .card-projects {
        width: 100%;
        align-self: center;
        // height: 30%;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 3rem;
        .card-project {
            position: relative;
            background-color: var(--sectionBack);
            width: 350px;
            height: 300px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 20px 20px 40px;
            border-radius: 10px;
            transition: 0.3s;
        }
    }
}

.card-project:hover {
    transform: translateY(-15px);
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.image {
    width: 100%;
    height: 60%;
    display: grid;
    place-content: center;
}
.image img {
    width: 240px;
}
.namePrice {
    width: 100%;
    display: flex;
    justify-content: space-between;
}
.namePrice h3 {
    font-size: 2em;
    text-transform: capitalize;
    color: var(--textColor);
}
.namePrice span {
    font-size: 1.5em;
    color: var(--starColor);
}
.card-project p {
    font-size: 18px;
    line-height: 25px;
}
.stars svg {
    font-size: 1.3em;
    color: var(--starColor);
}
.bay {
    position: absolute;
    bottom: 20px;
    right: 20px;
}
.bay button {
    padding: 10px 20px;
    border-radius: 7px;
    border: none;
    background-color: var(--textColor);
    color: var(--sectionBack);
    font-size: 18px;
    text-transform: capitalize;
    cursor: pointer;
    transition: 0.5s;
}
.bay button:hover {
    transform: scale(1.1);
}
</style>
