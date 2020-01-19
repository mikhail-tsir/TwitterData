import React from "react";

import Titles from "./components/Titles";
import Form from "./components/Form";
import Weather from "./components/Weather"


const api_key = "dd456f9212f065ab8678656adea8ada4";


class App extends React.Component{
    state = {
        sentiment_avg: undefined,
        pos: undefined,
        neg: undefined,
        error: undefined
    }
    getWeather = async(e) => {
        e.preventDefault();
        const keyword = e.target.elements.keyword.value;
        const random = {
            "sentiment_avg": "0.2",
            "positive_keywords": ["Apple", "Donald", "Duck", "Fat"],
            "neg_keywords": ["food", "math", "movie"]
          }


        if (keyword) {
            
            this.setState({
                sentiment_avg: random.sentiment_avg,
                pos: random.positive_keywords,
                neg: random.neg_keywords,
                error: ""
            });
        } else {
            this.setState({
                sentiment_avg: undefined,
                pos: undefined,
                neg: undefined,
                error: "Please enter a keyword."
            });
        }
    }
    render(){
        return(
            <div>
                <div className="back">
                    <div className="main">
                        <div className="container">
                            <div className="row">
                                <div className="col-xs-7 form-box">
                                    <Form getWeather={this.getWeather}/>
                                    <Weather 
                                        sentiment_avg={this.state.sentiment_avg}
                                        pos={this.state.pos}
                                        neg={this.state.neg}
                                        error={this.state.error}
                                    />
                                </div>
                                <div className="col-xs-5 title-box">
                                    <Titles />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
};

export default App;