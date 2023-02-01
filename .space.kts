job("Warmup data for PyCharm") {
    startOn {
        gitPush {
            branchFilter {
                +"refs/heads/master"
            }
        }
    }
    warmup(ide = Ide.PyCharm) {
        scriptLocation = "./dev-env-warmup.sh"
        devfile = ".space/devfile.yaml"
        ideVersion = IdeVersion.LatestOfQuality("EAP")
    }
}
