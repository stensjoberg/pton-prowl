import React, { Component } from 'react'
import Radium from 'radium'
import CourseBox from './CourseBox'
import { styles } from './styles'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class CourseBoxList extends Component {
  state = {
    courses: [],
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://0.0.0.0:8000/api/v1/courses/');
      const courses = await res.json();
      this.setState({
        courses
      });
      console.log(courses)
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div className="flexcontainer vert">
      {this.state.courses.map((item, i) => (
        <CourseBox
          key={item.id}
          id={item.id}
          title={item.title}
          i={i}
        />
      ))}
      </div>
    );
  }
}

export default Radium(CourseBoxList)
