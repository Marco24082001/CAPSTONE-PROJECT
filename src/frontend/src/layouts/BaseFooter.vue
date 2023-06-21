<template>
    <footer class="footer">
        <div class="footer-content">
            <h3>a wonderful gift</h3>
            <p>Convenient, reliable and transparent online crowdfunding platform.</p>
            <ul class="socials">
                <li>
                    <a href="#"><i class="bx bxl-instagram-alt"></i></a>
                </li>
                <li>
                    <a href="#"><i class="bx bxl-facebook-circle"></i></a>
                </li>
                <li>
                    <a href="#"><i class="bx bxl-google"></i></a>
                </li>
                <li>
                    <a href="#"><i class="bx bxl-youtube"></i></a>
                </li>
            </ul>
        </div>
        <div class="footer-bottom">
            <p>Capstone project &copy;2023 wondergift. designed by <span>marco</span></p>
        </div>
    </footer>
</template>
<script>
export default {
    name: "base-footer",
};
</script>
<style scoped lang="scss">
footer {
    z-index: 1000000;
    background-color: var(--cs-color-footer-background);
    height: auto;
    width: 100vw;
    font-family: "Open Sans";
    padding-top: 1rem;
    margin-top: 4rem;
    color: var(--cs-color-primary);
    .footer-content {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        text-align: center;
        h3 {
            font-size: 1.3rem;
            font-weight: 400;
            text-transform: capitalize;
            line-height: 3rem;
        }
        p {
            max-width: 500px;
            margin: 10px auto;
            line-height: 1rem;
            font-size: 0.9rem;
        }
        .socials {
            list-style: none;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0.2rem 0 1rem 0;
            li {
                margin: 0 10px;
            }
            a {
                text-decoration: none;
                color: #020202;
                i {
                    font-size: 0.9rem;
                    transition: color 0.4s ease;
                }
                &:hover i {
                    color: aqua;
                }
            }
        }
    }
    .footer-bottom {
        // background-color: #000;
        width: 100vw;
        padding: 20px 0;
        text-align: center;
        p {
            font-size: 0.9rem;
            word-spacing: 2px;
            text-transform: capitalize;
        }
        span {
            text-transform: uppercase;
            font-weight: 200;
        }
    }
}
</style>
