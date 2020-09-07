import React, { Component } from 'react'
import './Footer.css'
import { MDBCol, MDBContainer, MDBRow, MDBFooter } from "mdbreact";
export class Footer extends Component {
    render() {
        return (
            <div className="footer">
            <MDBFooter color="blue" className="font-small pt-4 mt-4">
              <MDBContainer fluid className="text-center text-md-left">
                <MDBRow>
                  <MDBCol md="6">
                    <h5 className="title">M & M Enterprises</h5>
                    <p>
                      Email: mukesh.ice17@gmail.com
                    </p>
                    <p>Mob: 9540339805</p>
                  </MDBCol>
                  <MDBCol md="6">
                    <h5 className="title">Links</h5>
                    <ul>
                      <li className="list-unstyled">
                        <a href="https://maurya20.github.io/rrt/">Sample Trading Info Website</a>
                      </li>
                      <li className="list-unstyled">
                        <a href="https://maurya20.github.io/amb_website/">Sample Company Info Website</a>
                      </li>
                    </ul>
                  </MDBCol>
                </MDBRow>
              </MDBContainer>
              <div className="footer-copyright text-center py-3">
                <MDBContainer fluid>
                  &copy; {new Date().getFullYear()} Copyright: <a href="https://github.com/maurya20"> M & M  </a>
                </MDBContainer>
              </div>
            </MDBFooter>
            </div>
        )
    }
}

export default Footer
