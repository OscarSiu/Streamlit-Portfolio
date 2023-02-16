import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #30b7b4;">
    <img src= "https://i.postimg.cc/2ST8n1ZF/logo.png">

    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
    <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
    <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
    </li>
    </ul>
    </div>
    </nav>
    """, unsafe_allow_html=True)

def st_button(icon, url, label, iconsize):
    if icon == 'notion':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
                <path fill="currentColor" d="M5.948 5.609c.99.807 1.365.75 3.234.625l17.62-1.057c.375 0 .063-.375-.063-.438l-2.927-2.115c-.557-.438-1.307-.932-2.74-.813L4.015 3.061c-.625.057-.75.37-.5.62zm1.057 4.11v18.536c0 .995.495 1.37 1.615 1.307l19.365-1.12c1.12-.063 1.25-.745 1.25-1.557V8.474c0-.813-.313-1.245-1-1.182L8.001 8.474c-.75.063-.995.432-.995 1.24zm19.115.989c.125.563 0 1.12-.563 1.188l-.932.188v13.682c-.813.438-1.557.688-2.177.688c-1 0-1.25-.313-1.995-1.245l-6.104-9.583v9.271l1.932.438s0 1.12-1.557 1.12l-4.297.25c-.125-.25 0-.875.438-.995l1.12-.313V13.142l-1.557-.125c-.125-.563.188-1.37 1.057-1.432l4.609-.313l6.354 9.708v-8.589l-1.62-.188c-.125-.682.37-1.182.995-1.24zM2.583 1.38L20.328.073c2.177-.188 2.74-.063 4.109.932l5.667 3.984c.932.682 1.245.87 1.245 1.615v21.839c0 1.37-.5 2.177-2.24 2.302L8.494 31.99c-1.302.063-1.927-.125-2.615-.995l-4.172-5.417C.962 24.583.65 23.838.65 22.969V3.558c0-1.12.5-2.052 1.932-2.177z"/>
                </svg> 
                {label}
            </a>
        </p>'''
    elif icon == 'git':
        button_code = f'''
        <p>
        <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
            <g fill="none"><g clip-path="url(#svgIDa)">
            <path fill="currentColor" fill-rule="evenodd" d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385c.6.105.825-.255.825-.57c0-.285-.015-1.23-.015-2.235c-3.015.555-3.795-.735-4.035-1.41c-.135-.345-.72-1.41-1.23-1.695c-.42-.225-1.02-.78-.015-.795c.945-.015 1.62.87 1.845 1.23c1.08 1.815 2.805 1.305 3.495.99c.105-.78.42-1.305.765-1.605c-2.67-.3-5.46-1.335-5.46-5.925c0-1.305.465-2.385 1.23-3.225c-.12-.3-.54-1.53.12-3.18c0 0 1.005-.315 3.3 1.23c.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23c.66 1.65.24 2.88.12 3.18c.765.84 1.23 1.905 1.23 3.225c0 4.605-2.805 5.625-5.475 5.925c.435.375.81 1.095.81 2.22c0 1.605-.015 2.895-.015 3.3c0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12Z" clip-rule="evenodd"/>
            </g><defs><clipPath id="svgIDa"><path fill="#fff" d="M0 0h24v24H0z"/></clipPath></defs></g>
            </svg>
            {label}
        </a>
        </p>'''
    elif icon == 'linkedin':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
                {label}
            </a>
        </p>''' 

    elif icon == '':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                {label}
            </a>
        </p>'''
    return st.markdown(button_code, unsafe_allow_html=True)
