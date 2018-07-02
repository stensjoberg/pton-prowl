import React, { Component } from 'react'
import Radium from 'radium'
import { styles } from './styles'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class CourseBox extends Component {
  handleAddition = () => {
    console.log(this.props.id)
    try {
      const res = fetch('http://0.0.0.0:8000/api/v1/courses/');
      const courses = res.json();
      this.setState({
        courses
      });
    } catch (e) {
      console.log(e);
    }
  }


  render() {
    return (
      <div className="flexcontainer hor coursebox" style={Object.assign({},
        this.props.i % 2 && styles.tigerStripe
      )}>
        <p>
          {this.props.title}
        </p>
        <button onClick={this.handleAddition}>
          +
        </button>
      </div>
    );
  }
}

export default Radium(CourseBox)
