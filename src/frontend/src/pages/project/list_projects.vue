<template>
    <div class="container">
        <div class="card-projects">
            <div class="card-project">
                <a
                    href="https://givenow.vn/du-an/chung-tay-cham-soc-suc-khoe-cho-200-tre-nhap-cu-tai-truong-tinh-thuong-ai-linh/"
                    class="image-index"
                >
                    <img src="@/assets/project_img/project-0.jpg" alt="" />
                </a>
                <div class="card-content">
                    <h3>Chung tay hỗ trợ học</h3>
                    <!-- <span>$ 15.99</span> -->
                </div>
                <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
            </div>

            <div class="card-project">
                <div class="image-index">
                    <img src="@/assets/project_img/project-2.png" alt="" />
                </div>
                <div class="card-content">
                    <h3>Chung tay hỗ trợ học</h3>
                    <!-- <span>$ 15.99</span> -->
                </div>
                <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
            </div>

            <div class="card-project">
                <div class="image-index">
                    <img src="@/assets/project_img/project-3.jpg" alt="" />
                </div>
                <div class="card-content">
                    <div class="card-meta">Cộng đồng</div>
                    <h3 class="card-title">Chung tay hỗ trợ học</h3>
                    <div class="target">400.000.000$</div>
                    <div class="card-author"><a href="#"> Quỹ học bổng Võ Thành Vĩ </a></div>
                    <!-- <span>$ 15.99</span> -->
                </div>
                <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
            </div>

            <div class="card-project">
                <div class="image-index">
                    <img src="@/assets/project_img/project-4.png" alt="" />
                </div>
                <div class="card-content">
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
        height: 65vh;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 3rem;
        .card-project {
            position: relative;
            background-color: var(--sectionBack);
            width: 15rem;
            height: 80%;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            // padding: 20px 20px 40px;
            transition: 0.3s;
            &:hover {
                transform: translateY(-15px);
                box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
            }
            .image-index {
                display: grid;
                overflow: hidden;
                place-content: center;
                height: 40%;
                img {
                    width: 100%;
                }
            }
            .card-content {
                width: 100%;
                display: flex;
                justify-content: space-between;
            }
        }
    }
}

// .card-content span {
//     font-size: 1.5em;
//     color: var(--starColor);
// }
// .card-project p {
//     font-size: 18px;
//     line-height: 25px;
// }
// .stars svg {
//     font-size: 1.3em;
//     color: var(--starColor);
// }
// .bay {
//     position: absolute;
//     bottom: 20px;
//     right: 20px;
// }
// .bay button {
//     padding: 10px 20px;
//     border-radius: 7px;
//     border: none;
//     background-color: var(--textColor);
//     color: var(--sectionBack);
//     font-size: 18px;
//     text-transform: capitalize;
//     cursor: pointer;
//     transition: 0.5s;
// }
// .bay button:hover {
//     transform: scale(1.1);
// }
</style>
