job("Warmup data for Fleet") {
    startOn {
        gitPush {
            branchFilter {
                +"refs/heads/master"
            }
        }
    }
    warmup(ide = Ide.Fleet) {
        scriptLocation = "./dev-env-warmup.sh"
        ideVersion = IdeVersion.LatestOfQuality("Stable")
    }
}

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
        ideVersion = IdeVersion.LatestOfQuality("Release")
    }
}
