import React from "react";
import Logo from "./real.png";

const Titles = () => (
    <div>
        <div>
            <h1 className="main_title">tweet<span className="black">Back</span></h1>
            <img src={Logo} alt="Smiley face" height="50" width="55"></img>
        </div>
        <p className="sub_title">Tweet Sentiment Analysis</p>
    </div>
);

export default Titles;