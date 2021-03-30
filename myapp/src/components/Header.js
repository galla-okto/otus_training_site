import { Component } from "react";

export class Header extends Component {
    render() {
        const { value } = this.props;

        return value > 5 ? <h1>{value}</h1> : <h4>{value}</h4>
    }
}

