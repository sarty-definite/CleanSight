import taipy as tp
from taipy import Config, Core, Gui
from taipy.gui import Html
################################################################
#            Configure application                             #
################################################################
def build_message(name):
    return f"Hello {name}!"


# A first data node configuration to model an input name.
input_name_data_node_cfg = Config.configure_data_node(id="input_name")
# A second data node configuration to model the message to display.
message_data_node_cfg = Config.configure_data_node(id="message")
# A task configuration to model the build_message function.
build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
# The scenario configuration represents the whole execution graph.
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

################################################################
#            Design graphical interface                        #
################################################################

input_name = "Taipy"
message = None
roles={
  "user1": ["role1", "TAIPY_READER"],
  "user2": ["role2", "TAIPY_ADMIN"],
  "user3": ["role1", "role2", "TAIPY_ADMIN"]
}
passwords={
  "user1@gmail.com": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
  "user2@gmail.com": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
}
# authenticator = Authenticator("taipy", roles=roles)
def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit()
    state.message = scenario.message.read()
Email=""
Password=""
def submit_login(state):
    global Email
    global Password
    Email=state.Email
    Password=state.Password


page = Html('''
    <!doctype html>
<html lang="en" data-bs-theme="auto">
  <head><script src="../assets/js/color-modes.js"></script>

    <meta charset="utf-8"></meta>
    <meta name="viewport" content="width=device-width, initial-scale=1"></meta>
    <meta name="description" content=""></meta>
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors"></meta>
    <meta name="generator" content="Hugo 0.118.2"></meta>
    <title>Signin Template · Bootstrap v5.3</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/sign-in/"></link>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3"></link>


<link href="../assets/dist/css/bootstrap.min.css" rel="stylesheet"></link>

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }

      .b-example-divider {
        width: 100%;
        height: 3rem;
        background-color: rgba(0, 0, 0, .1);
        border: solid rgba(0, 0, 0, .15);
        border-width: 1px 0;
        box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
      }

      .b-example-vr {
        flex-shrink: 0;
        width: 1.5rem;
        height: 100vh;
      }

      .bi {
        vertical-align: -.125em;
        fill: currentColor;
      }

      .nav-scroller {
        position: relative;
        z-index: 2;
        height: 2.75rem;
        overflow-y: hidden;
      }

      .nav-scroller .nav {
        display: flex;
        flex-wrap: nowrap;
        padding-bottom: 1rem;
        margin-top: -1px;
        overflow-x: auto;
        text-align: center;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
      }

      .btn-bd-primary {
        --bd-violet-bg: #712cf9;
        --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

        --bs-btn-font-weight: 600;
        --bs-btn-color: var(--bs-white);
        --bs-btn-bg: var(--bd-violet-bg);
        --bs-btn-border-color: var(--bd-violet-bg);
        --bs-btn-hover-color: var(--bs-white);
        --bs-btn-hover-bg: #6528e0;
        --bs-btn-hover-border-color: #6528e0;
        --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
        --bs-btn-active-color: var(--bs-btn-hover-color);
        --bs-btn-active-bg: #5a23c8;
        --bs-btn-active-border-color: #5a23c8;
      }

      .bd-mode-toggle {
        z-index: 1500;
      }

      .bd-mode-toggle .dropdown-menu .active .bi {
        display: block !important;
      }
    </style>

    
    <!-- Custom styles for this template -->
    <link href="sign-in.css" rel="stylesheet"></link>
  </head>
  <body class="d-flex align-items-center py-4 bg-body-tertiary">
    
<main class="form-signin w-100 py-10 m-auto">
  <form>
    <img class="" src="logo.png" alt="" style="margin-top:10rem;" width="400" height="100"></img>
    <h1 class="h1 mb-3 fw-normal">Please sign in</h1>

    <div class="form-floating">
      <label style="font-size:1.3rem" for="floatingInput">Email address</label><br></br>
      <taipy:input style="font-size:1rem;width:20rem;">{Email}</taipy:input>
    </div>
    <div class="form-floating">
      <label style="font-size:1.3rem" for="floatingPassword">Password</label><br></br>
      <taipy:input  password >{Password}</taipy:input>
    </div>
    <taipy:button style="Margin-top:1rem" on_action="submit_login">Log In</taipy:button>

  </form>
  </main>

    </body>
</html>

''')
stylekit = {
  "color_primary": "#ff6666",
  "color_secondary": "#ffffff",
}

if __name__ == "__main__":
    ################################################################
    #            Instantiate and run Core service                  #
    ################################################################
    Core().run()
    print("hello")
    ################################################################
    #            Manage scenarios and data nodes                   #
    ################################################################
    scenario = tp.create_scenario(scenario_cfg)
    ################################################################
    #            Instantiate and run Gui service                   #
    ################################################################
    
    Gui(page).run(stylekit=stylekit, update_interval=0.1)

